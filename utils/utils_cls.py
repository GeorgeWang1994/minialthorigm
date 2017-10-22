# -*- coding: utf-8 -*-

import inspect

import enum
from django.db import models
from django.test import Client
import json


class ChoiceEnum(enum.Enum):
    """
    封装enum，可以在Model中的choice中使用
    """
    @classmethod
    def choices(cls):
        user_members = inspect.getmembers(object=cls, predicate=lambda m: not inspect.isroutine(m))
        props = [m for m in user_members if not (m[0][:2] == '__')]
        choices = tuple((m[1].name, m[1].value) for m in props)
        return choices


class BaseModel(models.Model):
    """
    所有Model都要继承的基类
    """
    created_time = models.DateTimeField(auto_now_add=True, db_index=True, help_text=u'创建时间')  # 对创建时间创建索引
    last_modified = models.DateTimeField(auto_now=True, help_text=u'最近修改时间')
    is_deleted = models.BooleanField(default=False, help_text=u'是否已经删除')

    class Meta:
        abstract = True


class CustomClient(Client):
    """
    继承了Django中的Client，添加两种json的方法
    """
    def json_get(self, path, data=None):
        data = data or {}
        if '?' not in path:
            path += '?'
        response = self.get(path, data)
        return json.loads(response.content)

    def json_post(self, path, data=None):
        data = data or {}
        response = self.post(path, data)
        return json.loads(response.content)
