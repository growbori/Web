from django.db import models

# Create your models here.
# OOPs 7일차 8일차 복습 필요
class Article(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    # 파일을 생성하거나 갱신할 경우 그 때의 데이터가 자동으로 입력됨
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


# 최종 테이블 이름은 앱이름_모델클래스이름으로 합성해서 만듦