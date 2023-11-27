import paho.mqtt.client as mqtt

# Configurações do broker MQTT
broker_address = "broker.hivemq.com"  # Substitua pelo endereço do seu broker MQTT
port = 1883  # Porta padrão MQTT
topic = "exame/ecg/iot2023"  # Substitua pelo tópico que você deseja assinar

# Função de callback para quando a conexão é estabelecida
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado ao broker MQTT")
        # Inscreva-se ao tópico desejado quando a conexão é estabelecida
        client.subscribe(topic)
    else:
        print(f"Falha na conexão, código de retorno: {rc}")

# Função de callback para quando uma mensagem é recebida
def on_message(client, userdata, message):
    print(f"Mensagem recebida no tópico '{message.topic}': {message.payload.decode()}")

# Crie um cliente MQTT
client = mqtt.Client()

# Configure as funções de callback
client.on_connect = on_connect
client.on_message = on_message

# Conecte-se ao broker MQTT
client.connect(broker_address, port=port, keepalive=60)

# Mantenha o cliente em execução para receber mensagens
client.loop_forever()
