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

        print("---------test_create---------")

        response = self.client.post(self.base_url + "/user/register/", data=self.user)
        print("---------register-----response.status_code---------")
        self.assertEqual(response.status_code, 201)
        print("---------register-----response.data---------", response.data)

    def test_login(self):
        print("---------test_login---------")
        self.user.pop("nickname")

        response = self.client.post(self.base_url + "/user/login/", data=self.user)
        print("---------login-----response.status_code---------")
        self.assertEqual(response.status_code, 200)
