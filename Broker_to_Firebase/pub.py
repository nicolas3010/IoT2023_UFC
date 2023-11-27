import paho.mqtt.publish as publish

# Configurações MQTT
mqtt_broker = "broker.hivemq.com"  # Substitua pelo endereço do seu broker MQTT
mqtt_topic = "exame/ecg/iot2023"  # Substitua pelo tópico desejado
print(len("1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;"))

# String a ser enviada
mensagem = "1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;1.67;1.76;1.73;1.67;1.73;1.80;1.68;1.70;1.83;1.73;1.71;1.87;1.85;1.77;1.83;1.91;1.80;1.83;1.97;1.88;."

# Publica a mensagem
publish.single(mqtt_topic, mensagem, hostname=mqtt_broker)

print("Mensagem de string enviada com sucesso.")