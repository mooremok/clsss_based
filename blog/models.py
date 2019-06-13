from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('标题', max_length=100)
    summary = models.CharField('摘要', max_length=1000)
    body = models.TextField('内容')
    created_time = models.DateTimeField('时间', auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '文章'

    def __str__(self):
        return self.title
