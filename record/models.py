from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Record(models.Model):
    class Kind(models.TextChoices):
        """
        운동 종류

        class로 만든 이유는 TypeSafe한 선택지를 사용하고 싶기 때문이다
        단순히 튜플로 정의했을 경우, 잘못된 인덱스 접근이 발생할 수 있고 오타로 인해 잘못된 값이 들어갈 수 있으므로, 클래스로 만들어서 휴먼 에러가 발생할 여지를 줄임
        """

        RUN = "RUN", "걷기"
        WALK = "WALK", "뛰기"
        BICYCLE = "BICYCLE", "자전거"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_at = models.DateTimeField(blank=True, null=True)
    end_at = models.DateTimeField(blank=True, null=True)
    static_map = models.ImageField(
        upload_to="record/static_map/%Y/%m/%d/", blank=True, null=True
    )
    coords = models.TextField(help_text="GPS데이터", blank=True, null=True)
    distance = models.FloatField(help_text="운동한 거리", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    kind = models.CharField(
        choices=Kind, max_length=10, default=Kind.RUN, help_text="운동 종류"
    )

    def __str__(self):
        return f"{self.user}: {self.start_at}"

    class Meta:
        db_table = "records"
        verbose_name = "운동 기록"


class RecordImage(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="record/images/%Y/%m/%d/")

    def __str__(self):
        return f"{self.record} - {self.image}"

    class Meta:
        db_table = "record_images"
        verbose_name = "인증샷"
