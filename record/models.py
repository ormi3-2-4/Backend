from django.db import models
from django.contrib.auth import get_user_model

class Record(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    start_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(blank=True, null=True)
    static_map = models.ImageField(upload_to='record/static_map/%Y/%m/%d/')
    coords = models.TextField(help_text='GPS데이터')
    distance = models.FloatField(help_text='운동한 거리')
    speed = models.FloatField(help_text='평균 속력')
    kind = models.CharField(help_text='enum(walk, run, bicycle)', max_length=50) 

    def __str__(self):
        return f'{self.user}: {self.start_at}'

    class Meta:
        verbose_name = '운동 기록'

class RecordImage(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='record/images/%Y/%m/%d/')

    def __str__(self):
        return f'{self.record} - {self.image}'

    class Meta:
        verbose_name = '인증샷'