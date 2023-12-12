from django.db import models


class Record(models.Model):
  user_id = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add=True)
  last_update = models.DateTimeField(auto_now=True)
  finished_at = models.DateTimeField(blank=True, null=True)
  static_map = models.ImageField(upload_to='record/static_map/%Y/%m/%d/')
  data = models.TextField(help_text='GPS데이터')
  distance = models.FloatField(help_text='운동한 거리')
  speed = models.FloatField(help_text='평균 속력')
  kind = models.CharField(help_text='운동 종류', max_length=50)
  
  def __str__(self):
    return f'{self.user_id}: {self.created_at}'

  class Meta:
    verbose_name = '운동 기록'
