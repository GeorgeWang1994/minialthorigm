# -*- coding: utf-8 -*-

from like.models import Like
from account.testing.mock import create_user
from chat.testing.mock import create_post
from chat.models import PostTypeChoiceEnum


def create_like(user=None, post=None, post_type=PostTypeChoiceEnum.POST):
    user = user or create_user()
    post = post or create_post(author=user)

    return Like.objects.create(user_id=user.id, post_id=post.id, post_type=post_type)
