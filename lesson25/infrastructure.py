import requests
import json
import random


class Phone:
    def __init__(self):
        self.base_url = 'https://api.restful-api.dev/objects'
        self.headers = {'content-type':'application/json'}
        self.upadted_name = {"name":"New Cool Name Turbo 3000"}
        self.updated_data_correct_one = {"data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "worth it": "No"
            }}
        self.updated_data_incorrect_one = {"data":{"year": 2020}}
        self.default_phone_data = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9"
   }
}
        self.default_phone_update_data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "worth it": "defenitely yes"
            }
        }

    def get_list_of_all_objects(self):
        return requests.get(self.base_url)

    def get_single_phone(self, device_id):
        return requests.get(f'{self.base_url}/{device_id}')

    def create_single_default_object(self):
        return requests.post(self.base_url, headers=self.headers, data=json.dumps(self.default_phone_data))

    def update_single_default_object(self):
        response_of_single_created_object = self.create_single_default_object()
        return requests.put(f'{self.base_url}/{response_of_single_created_object.json()["id"]}',
                            headers=self.headers,
                            data=json.dumps(self.default_phone_update_data))

    def patch_single_default_object(self, patched_data):
        response_of_single_created_object = self.create_single_default_object()
        return requests.patch(f'{self.base_url}/{response_of_single_created_object.json()["id"]}',
                            headers=self.headers,
                            data=json.dumps(patched_data))


    def delete_default_object(self):
        response_of_single_created_object = self.create_single_default_object()
        obj_id = response_of_single_created_object.json()["id"]
        return requests.delete(f'{self.base_url}/{obj_id}'), obj_id


dogs_names = ['Pes Patron', 'Gerda', 'Woof', 'Rex', 'Good Boy']
colours = ['black', 'white','dirt', 'mixed', 'beautiful']
mass = [2,4,6,8,10,20,200]

class Dog:
    base_url = 'https://api.restful-api.dev/objects'
    def __init__(self):

        self.headers = {'content-type': 'application/json'}
        self.dog_data = {'name':random.choice(dogs_names),
                         'data':{
                             'colour':random.choice(colours),
                             'mass':random.choice(mass)
                         }}
        self.object_response = requests.post(url=self.base_url,headers=self.headers, data=json.dumps(self.dog_data))
        self._id = self.object_response.json()['id']
        self.created_time = self.object_response.json()['createdAt']

    @classmethod
    def genreate_dogs_pack(cls):
        list_of_dogs = []
        for i in range(random.randint(4,15)):
            list_of_dogs.append(cls())
        return list_of_dogs

    @classmethod
    def filter_only_dogs(cls, list_of_dogs):
        filtration_url = cls.base_url+'?'
        for dog in list_of_dogs:
            if dog != list_of_dogs[-1]:
                filtration_url +=f'id={dog._id}&'
            else:
                filtration_url += f'id={dog._id}'
        print(filtration_url)
        return requests.get(filtration_url)




