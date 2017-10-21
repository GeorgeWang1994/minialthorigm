# -*- coding: utf-8 -*-

from django.db import models
from utils.utils_cls import BaseModel


class PostLike(BaseModel):
    user_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    post_id = models.CharField(max_length=20, unique=True, help_text=u'文章id')
