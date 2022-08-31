from multiprocessing import dummy
import time
import random
import json
from datetime import datetime
from data_generator import generate_message
from kafka import KafkaProducer

#Messages will be serialized  as Json
def serializer(message):
    return json.dumps(message).encode('utf-8')

#Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['172.17.0.1:9092'],
    value_serializer=serializer
)

if __name__== '__main__':
    while True:
        dummy_message = generate_message()
        print(f'Producing message @ {datetime.now()} | Message = {str(dummy_message)}')
        producer.send('messages',dummy_message)

        time_to_sleep=random.randint(1,11)
        time.sleep(time_to_sleep)
