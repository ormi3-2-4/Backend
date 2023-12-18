from django.test import TestCase, Client
import json

from user.tests import UserTest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.gis.geos import LineString

# gdal 설치 필요
# brew install gdal (mac)
# sudo apt-get install binutils libproj-dev gdal-bin (window + WSL)
# yum --enablerepo=epel -y install gdal gdal-devel .config 파일에 추가 (AWS)
# https://oneone-note.tistory.com/42


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
        self.headers["Content-Type"] = "application/json"
        update_coords = [(37.123, 127.123), (37.123, 127.123), (37.123, 127.123), (37.123, 127.123), (37.123, 127.123)]
        
        self.record["coords"] = json.dumps(update_coords)
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
    
    def test_image_upload(self):
        print("---------test_image_upload---------")
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        response = self.client.post(self.base_url + "/record/" + str(self.record["id"]) + "/image/", headers=self.headers, data={"image": image})
        print("---------response.data---------")
        print(response.data)
            
        self.assertEqual(response.status_code, 201)
        
        self.test_record_detail()
    
    def test_calculate(self):
        print("---------test_calculate---------")
        self.headers["Content-Type"] = "application/json"
        update_coords = [(126.76514625549316, 37.64388603051884),(126.76929831504823, 37.64818454268491), (126.77118659019472, 37.64708870056084), (126.76916956901552, 37.64825250135397)]
        
        self.record["coords"] = json.dumps(update_coords)
        print("---------merged_coords---------")
        print(self.record)
        response = self.client.patch(self.base_url + "/record/" + str(self.record["id"]) + "/calculate/", headers=self.headers, data=json.dumps(self.record))
        print("---------response.status_code---------")
        
        print("---------response.data---------")
        print(response.data)
        self.assertEqual(response.status_code, 200)
        coords = json.loads(response.data["coords"])
        print("---------coords---------")
        for (lat, lng) in coords:
            print(lat, lng)
    
    def test_distance(self):
        print("---------test_distance---------")
        line = LineString([(126.76514625549316, 37.64388603051884),(126.76929831504823, 37.64818454268491), (126.77118659019472, 37.64708870056084), (126.76916956901552, 37.64825250135397)], srid=4326)

        print(round(line.length*1000, 2)) 
        