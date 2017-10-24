# -*- coding: utf-8 -*-

from django.db import models

from chat.models import PostTypeChoiceEnum
from utils.utils_cls import BaseModel


class Favor(BaseModel):
    user_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    post_id = models.CharField(max_length=20, unique=True, help_text=u'文章或者帖子id')
    post_type = models.CharField(max_length=100, default=PostTypeChoiceEnum.POST,
                                 choices=PostTypeChoiceEnum.choices(), help_text=u'文章类型')
