# -*- coding: utf-8 -*-

from django.db import models


class Article(models.Model):
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    title = models.CharField(max_length=120, help_text=u'标题')
    content = models.TextField(help_text=u'内容')
    like_count = models.IntegerField(default=0, help_text=u'点赞人数')
    comment_count = models.IntegerField(default=0, help_text=u'评论人数')
    create_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
