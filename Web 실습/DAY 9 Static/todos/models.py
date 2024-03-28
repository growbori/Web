from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 20)
    completed = models.BooleanField(default = False)
    is_editting = models.BooleanField(default = False)  # 수정중인지 판단
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now = True)