# -*- coding: utf-8 -*-

from django.db import models

from utils.utils_cls import BaseModel, ChoiceEnum


class LikeTypeChoiceEnum(ChoiceEnum):
    ARTICLE = "ARTICLE"
    POST = "POST"
    COMMENT = "COMMENT"


class Like(BaseModel):
    user_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    post_id = models.CharField(max_length=20, unique=True, help_text=u'文章或者帖子或者评论id')
    type = models.CharField(max_length=100, default=LikeTypeChoiceEnum.COMMENT,
                                 choices=LikeTypeChoiceEnum.choices(), help_text=u'点赞类型')
