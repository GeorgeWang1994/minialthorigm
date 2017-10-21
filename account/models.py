# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, primary_key=True, help_text=u'用户')
    comment_post_count = models.IntegerField(default=0, help_text=u'评论帖子个数')
    favor_post_count = models.IntegerField(default=0, help_text=u'收藏帖子个数')
