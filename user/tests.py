from django.test import TestCase, Client


# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.base_url = "http://localhost:8000"
        self.client = Client()

        print("---------user---------")
        self.user = {
            "nickname": "test",
            "email": "test@example.com",
            "password": "test1234",
        }
        print(self.user)

        self.test_register()
    def test_register(self):
        print("---------test_create---------")

        response = self.client.post(self.base_url + "/user/register/", data=self.user)
        print("---------register-----response.status_code---------")
        if response.status_code != 201:
            print("---------register-----response.data---------")
            print(response.data)
        self.assertEqual(response.status_code, 201)
        print("---------register-----response.data---------", response.data)
        self.token = response.data["data"]["token"]
        self.user_id = response.data["data"]["user"]["id"]
        self.headers = {}
        self.headers["Authorization"] = "Bearer " + self.token["access_token"]
        
    def test_login(self):
        print("---------test_login---------")
        self.user.pop("nickname")

        response = self.client.post(self.base_url + "/user/login/", data=self.user)
        print("---------login-----response.status_code---------")
        self.assertEqual(response.status_code, 200)