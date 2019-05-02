from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Topic(models.Model):
    topic = models.CharField('版', max_length=20)

    def __str__(self):
        return self.topic

class Sort(models.Model):
    sort = models.CharField('分類', max_length=2)

    def __str__(self):
        return self.sort

class Post(models.Model):
    topic = models.ForeignKey(Topic, models.CASCADE, verbose_name='版', related_name='topics')
    sort = models.ForeignKey(Sort, on_delete=models.PROTECT, verbose_name='分類', related_name='sorts')
    title = models.CharField('標題', max_length=15)
    content = models.TextField('內文')
    creater = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='發文者', related_name='posts')
    create_at = models.DateTimeField('建立時間', auto_now_add=True)
    update_at = models.DateTimeField('更新時間', auto_now=True)

    def __str__(self):
        return '{} {} Post create by {}'.format(
            self.sort,
            self.title,
            self.creater.username,
        )

class Option(models.Model):
    option = models.CharField('推/噓文', max_length=1)

    def __str__(self):
        return self.option

class Comment(models.Model):
    content = models.TextField('留言')
    creater = models.ForeignKey(User, models.CASCADE, verbose_name='留言者', related_name='comments')
    option = models.ForeignKey(Option, models.CASCADE, verbose_name='推/噓文', related_name='options')

    def __str__(self):
        return '{} {} Commit create by {}'.format(
            self.option,
            self.content,
            self.creater.username
            )

