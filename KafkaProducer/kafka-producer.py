from kafka import KafkaProducer
from json import dumps
import requests

producer = KafkaProducer(
   value_serializer=lambda m: dumps(m).encode('utf-8'), 
   bootstrap_servers=['kafka:9092'])

resp = requests.get('http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET Random Numbers {}'.format(resp.status_code))
for random_number in resp.json():
    producer.send("test", value={"Height": random_number})

producer.flush()