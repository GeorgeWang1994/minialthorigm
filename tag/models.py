# -*- coding: utf-8 -*-

from django.db import models

from utils.utils_cls import BaseModel


class Tag(BaseModel):
    content = models.CharField(max_length=20, unique=True, help_text=u'标签内容')
