# -*- coding: utf-8 -*-

from django.db import models
from utils.utils_cls import BaseModel


class PostComment(BaseModel):
    content = models.CharField(max_length=300, help_text=u'评论内容')
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    post_id = models.CharField(max_length=20, help_text=u'文章或者帖子id')
