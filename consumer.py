import json
from kafka import KafkaConsumer

if __name__ == '__main__':
    print('Consumer start')
    consumer=KafkaConsumer(
        'messages',
        bootstrap_servers='172.17.0.1:9092',
        auto_offset_reset='earliest'
    )

    for message in consumer:
        print('q')
        print(message.value)