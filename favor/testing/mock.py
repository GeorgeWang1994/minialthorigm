# -*- coding: utf-8 -*-

from favor.models import Favor
from chat.models import PostTypeChoiceEnum
from account.testing.mock import create_user
from chat.testing.mock import create_post


def create_favor(user=None, post=None, post_type=PostTypeChoiceEnum.POST):
    user = user or create_user()
    post = post or create_post(author=user)

    return Favor.objects.create(user_id=user.id, post_id=post.id, post_type=post_type)
