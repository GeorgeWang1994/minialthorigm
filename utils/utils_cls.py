# -*- coding: utf-8 -*-

import inspect
import enum


class ChoiceEnum(enum.Enum):
    @classmethod
    def choices(cls):
        user_members = inspect.getmembers(object=cls, predicate=lambda m: not inspect.isroutine(m))
        props = [m for m in user_members if not (m[0][:2] == '__')]
        choices = tuple((m[1].name, m[1].value) for m in props)
        return choices
