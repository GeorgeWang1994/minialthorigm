# -*- coding: utf-8 -*-

from django.db import models

from utils.utils_cls import BaseModel, ChoiceEnum


class PostTypeChoiceEnum(ChoiceEnum):
    ARTICLE = "ARTICLE"
    POST = "POST"


class Post(BaseModel):
    content = models.CharField(max_length=300, help_text=u'帖子内容')
    author_id = models.IntegerField(unique=True, help_text=u'用户id')
    favor_count = models.IntegerField(default=0, help_text=u'帖子收藏个数')
    comment_count = models.IntegerField(default=0, help_text=u'帖子评论个数')
    like_count = models.IntegerField(default=0, help_text=u'帖子点赞个数')
    view_count = models.IntegerField(default=1, help_text=u'阅览人数')
