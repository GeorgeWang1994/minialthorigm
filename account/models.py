# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from utils.utils_cls import BaseModel


class UserInfo(BaseModel):
    user = models.OneToOneField(User, primary_key=True, help_text=u'用户')
    comment_count = models.IntegerField(default=0, help_text=u'评论个数')
    favor_count = models.IntegerField(default=0, help_text=u'收藏个数')
    like_count = models.IntegerField(default=0, help_text=u'点赞个数')
