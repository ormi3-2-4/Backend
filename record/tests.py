from django.test import TestCase, Client
import json
from record.models import Record
from django.db.models.functions import Concat
from django.db.models import CharField, Value
from .serializers import RecordSerializer
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer, UserLoginSerializer
from user.tests import UserTest

# Create your tests here.
class RecordTest(UserTest):
    def setUp(self):
        super().setUp()
        self.base_url = "http://localhost:8000"
        self.client = Client()
        
        self.record = {
            "user": self.user,
            "kind": "RUN",
            "start_at": "2021-07-01T00:00:00",
            "end_at": "2021-07-01T00:00:00",
            "static_map": "http://localhost:8000/media/record/static_map/2021/07/01/running_1.jpg",
        }
        
        self.test_create()
        
    def test_create(self):
        print("---------test_create---------")
                
        response = self.client.post(self.base_url + "/record/", headers=self.headers, data={"user": self.user_id})
        
        print("---------response.status_code---------")
        if response.status_code != 201:
            print("---------response.data---------")
            print(response.data)
        self.assertEqual(response.status_code, 201)
        print("---------response.data---------")
        print(response.data)
        self.record = response.data
        
    def test_record_update(self):
        print("---------test_record_update---------")
        # self.user["email"] = "test2@example.com"
        # self.test_register()
        self.headers["Content-Type"] = "application/json"
        update_coords = [(37.123, 127.123), (37.123, 127.123), (37.123, 127.123), (37.123, 127.123), (37.123, 127.123)]
        
        self.record["coords"] = update_coords
    
        old_coords = self.record["coords"]
        merged_coords = old_coords + update_coords
        
        self.record["coords"] = json.dumps(merged_coords)
        print("---------merged_coords---------")
        print(self.record)
        response = self.client.patch(self.base_url + "/record/" + str(self.record["id"]) + "/", headers=self.headers, data=json.dumps(self.record))
        print("---------response.status_code---------")
        
        print("---------response.data---------")
        print(response.data)
        self.assertEqual(response.status_code, 200)
        coords = json.loads(response.data["coords"])
        print("---------coords---------")
        for (lat, lng) in coords:
            print(lat, lng)
            
    def test_record_delete(self):
        print("---------test_record_delete---------")
        response = self.client.delete(self.base_url + "/record/" + str(self.record["id"]) + "/", headers=self.headers)
        print("---------response.status_code---------")
        self.assertEqual(response.status_code, 204)
        
    def test_record_list(self):
        print("---------test_record_list---------")
        self.user["email"] = "test2@example.com"
        self.test_register()
        self.user["email"] = "test3@example.com"
        self.test_register()
        for i in range(20):
            self.user_id = i%3 + 1
            self.test_create()
        response = self.client.get(self.base_url + "/record/", headers=self.headers)
        print("---------response.status_code---------")
        self.assertEqual(response.status_code, 200)
        print("---------response.data---------")
        print(response.data)
        
    def test_record_detail(self):
        print("---------test_record_detail---------")
        response = self.client.get(self.base_url + "/record/" + str(self.record["id"]) + "/", headers=self.headers)
        print("---------response.status_code---------")
        if response.status_code != 200:
            print("---------response.data---------")
            print(response.data)
            
        self.assertEqual(response.status_code, 200)
        print("---------response.data---------")
        print(response.data)
    
    