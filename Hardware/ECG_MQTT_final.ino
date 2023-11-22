


#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


#include <WiFi.h>
#include <ArduinoMqttClient.h>

// Enable LW MQTT library after include the library and before include the FirebaseJson.
#include <FirebaseJson.h>

#include "driver/adc.h"
#include <esp_adc_cal.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

/* Define the WiFi credentials */
#define WIFI_SSID "Iot"
#define WIFI_PASSWORD "iot20231"

#define button    14
#define LED       13
#define LO_pos    25
#define LO_neg    33
#define ECG_OUT   32

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

unsigned long lastMillis = 0;

int count = 0;

const char broker[] = "broker.hivemq.com";
int port = 1883;
const char topic[] = "exame/ecg/iot2023";

esp_adc_cal_characteristics_t adc_chars;

unsigned long micros_pre = 0;
unsigned long micros_interval = 5000;

const long interval = 1000;
unsigned long previousMillis = 0;

bool mqttReady = false;


void setup()
{

  Serial.begin(115200);
  Wire.begin();

  pinMode(LED, OUTPUT);
  pinMode(LO_pos, INPUT); // Setup for leads off detection LO +
  pinMode(LO_neg, INPUT); // Setup for leads off detection LO -
  pinMode(button, INPUT_PULLUP);

  analogSetPinAttenuation(ECG_OUT, ADC_11db);
  esp_adc_cal_characterize(ADC_UNIT_1, ADC_ATTEN_DB_11, ADC_WIDTH_BIT_12, 1100, &adc_chars);

  //-----------Display LCD_1306-------------
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
  }else{
    
  }
  display.display();
  display.clearDisplay();
  delay(10);
  //------------------------------------------------------

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(00, 20);
  display.println("Iniciando");
  display.print("ECGiHealth");
  display.display();

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(250);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();
  digitalWrite(LED, HIGH);
  delay(250);
  digitalWrite(LED, LOW);
  delay(250);
  digitalWrite(LED, HIGH);
  delay(250);
  digitalWrite(LED, LOW);

  Serial.print("Attempting to connect to the MQTT broker: ");
  Serial.println(broker);

  if (!mqttClient.connect(broker, port))
  {
    Serial.print("MQTT connection failed! Error code = ");
    Serial.println(mqttClient.connectError());
    return;
  }
  mqttReady = true;


  Serial.println("You're connected to the MQTT broker!");
  digitalWrite(LED, HIGH);
  Serial.println();

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(02, 20);
  display.print("ECGiHealth ");
  display.display();
}

void loop()
{
  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(02, 20);
  display.print("ECGiHealth ");
  display.display();

  
  if (!mqttReady)
    return;

  mqttClient.poll();

  if(digitalRead(button) == 0){
      mqtt();
  }

  Serial.println(digitalRead(button));
}

String ECG() {

  Serial.println("ECG...");

  display.clearDisplay();
  display.setTextSize(2);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(00, 20);
  display.print("Realizando  exame... ");
  display.display();

  int c = 0;
  int time_delay   = 2;
  int stop_reading = micros_interval / time_delay;
  String ecg_data = "";

  while (c < stop_reading) {

    if ((digitalRead(LO_pos) == 1) || (digitalRead(LO_neg) == 1)) {
      // Serial.println('!');
    }
    else {
      uint32_t  s = analogRead(ECG_OUT);
      uint32_t sinal = esp_adc_cal_raw_to_voltage(s, &adc_chars);

      Serial.print("Sinal_ECG:");
      Serial.println(sinal / 1000.00);

      ecg_data += String(sinal / 1000.00) + ";";

    }
    c++;
    delay(time_delay);
  }
  Serial.println("end");

  return ecg_data;

}

void mqtt() {
  Serial.print("Sending message to topic: ");
  Serial.println(topic);
  FirebaseJson json;

  json.add(ECG());

  // json.add("def", count % 5 == 0);
  json.toString(Serial);
  Serial.println();

  // send message, the Print interface can be used to set the message contents
  mqttClient.beginMessage(topic);
  json.toString(mqttClient);
  mqttClient.endMessage();
}
