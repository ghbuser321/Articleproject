from django.db import models

from accounts.models import CustomUser
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ', max_length=20)

    def __str__(self):
        return self.title

class PhotoPost(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=200)

    comment_1=models.TextField(verbose_name='コメント1',blank=True, null=True)
    #さらにコメントを追加
    comment_2=models.TextField(verbose_name='コメント2',blank=True, null=True)
    image1 = models.ImageField(verbose_name='イメージ1', upload_to = 'makes')
    image2 = models.ImageField(verbose_name='イメージ2', upload_to='makes',blank=True, null=True)
    #動画を追加するモデル
    video = models.FileField(verbose_name='動画',upload_to='videos',blank=True, null=True)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)

    def __str__(self):
        return self.title

