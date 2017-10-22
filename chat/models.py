# -*- coding: utf-8 -*-

from django.db import models

from utils.utils_cls import BaseModel


class Post(BaseModel):
    content = models.CharField(max_length=300, help_text=u'帖子内容')
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    like_count = models.IntegerField(default=0, help_text=u'帖子点赞个数')
    comment_count = models.IntegerField(default=0, help_text=u'帖子评论个数')
