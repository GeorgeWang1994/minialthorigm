# -*- coding: utf-8 -*-

from django.db import models

from chat.models import LikeTypeChoiceEnum
from utils.utils_cls import BaseModel


class Like(BaseModel):
    user_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    post_id = models.CharField(max_length=20, unique=True, help_text=u'文章或者帖子或者评论id')
    post_type = models.CharField(max_length=100, default=LikeTypeChoiceEnum.COMMENT,
                                 choices=LikeTypeChoiceEnum.choices(), help_text=u'点赞类型')
