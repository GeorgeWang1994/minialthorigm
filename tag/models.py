# -*- coding: utf-8 -*-

from django.db import models

from chat.models import PostTypeChoiceEnum
from utils.utils_cls import BaseModel


class Tag(BaseModel):
    user_id = models.IntegerField(help_text=u'创建者')
    content = models.CharField(max_length=20, unique=True, help_text=u'标签内容')


class PostTag(BaseModel):
    post_id = models.IntegerField(help_text=u'文章或帖子id')
    tag = models.ForeignKey(Tag, help_text=u'标签')
    post_type = models.CharField(max_length=100, default=PostTypeChoiceEnum.POST,
                                 choices=PostTypeChoiceEnum.choices(), help_text=u'文章类型')
