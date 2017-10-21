# -*- coding: utf-8 -*-

from django.db import models
from utils.utils_cls import ChoiceEnum, BaseModel


class FeedBackChoiceEnum(ChoiceEnum):
    CATON = u'卡顿'
    BUG = u'有BUG'
    NO_HELP = u'没有帮助'
    NO_REASON = u'没有其他原因'


class FeedBack(BaseModel):
    content = models.TextField(max_length=300, blank=False, null=False, help_text=u'评论内容')
    user_id = models.CharField(max_length=100, db_index=True, unique=True, help_text=u'用户id')
    choice = models.CharField(max_length=100, default=FeedBackChoiceEnum.NO_REASON, choices=FeedBackChoiceEnum.choices(),
                              help_text=u'反馈选择')
