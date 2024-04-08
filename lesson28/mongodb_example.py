from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bson

url = 'mongodb+srv://Primat:d2z76ctb@cluster0.v1o4bs7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(url, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print('success')
except Exception as e:
    print(e)

sample_weatherdata = client.get_database('sample_weatherdata')
data = sample_weatherdata.get_collection('data')
print(data)
data_samples = data.find_raw_batches()
#for data_sample in data_samples:
#    print(bson.decode_all(data_sample))
one_datasample = data.find_one(filter={'type': 'FM-13'})
print(one_datasample)
value = data.insert_one({'city worth to live in':'Kharkiv'})
print(value)
check_if_inserted = data.find_one(value.inserted_id)
print(check_if_inserted)