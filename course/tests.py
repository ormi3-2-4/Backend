# Create your tests here.
from datetime import datetime, timedelta

from django.test.testcases import TestCase, Client
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from record.models import Record
from user.models import User


class CourseTest(TestCase):
    def setUp(self):
        print("==========setUp==========")

        self.client = Client()
        user = User.objects.create_user("test", "test@test.com", "test1234")
        user.save()
        self.user = user

        refresh_token = TokenObtainPairSerializer.get_token(user)
        access_token = str(refresh_token.access_token)
        self.access_token = access_token

        record = Record.objects.create(
            user=user,
            start_at=datetime.now(),
            end_at=datetime.now() + timedelta(hours=1),
            coords="(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)",
            distance=10,
            speed=10,
            kind=Record.Kind.RUN,
        )
        self.record = record
        print("=====================================")

    def test_course_create(self):
        print("==========test_course_create==========")
        course = {
            "title": "test",
            "content": "test",
            "record": 1,
            "tags": "test",
        }
        response = self.client.post(
            "/course/",
            data=course,
            headers={"Authorization": f"Bearer {self.access_token}"},
        )
        self.assertEqual(response.status_code, 201)
        print(response.data)
        print("=====================================")

    def test_get_all_course(self):
        print("==========test_get_all_course==========")
        response = self.client.get("/course/")
        self.assertEqual(response.status_code, 200)
        print(response.data)
        print("=====================================")

    testcase = [setUp, test_course_create, test_get_all_course]
