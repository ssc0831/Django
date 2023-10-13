from django.db import models
from datetime import datetime

# Create your models here.

class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.CharField(null=False, max_length=50)
    title = models.CharField(null=False, max_length=200)
    content = models.TextField(null=False)
    hit = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    filename = models.CharField(null=True, blank=True, default='', max_length=500)
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

# 조회수 증가
    def hit_up(self):
        self.hit += 1

# 파일 다운로드 수 증가
    def down_up(self):
        self.down += 1