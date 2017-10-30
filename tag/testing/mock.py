# -*- coding: utf-8 -*-

from tag.models import PostTag, Tag
from chat.models import PostTypeChoiceEnum
from chat.testing.mock import create_post
from account.testing.mock import create_user


def create_tag(user=None, content=''):
    user = user or create_user()
    content = content or '标签'
    return Tag.objects.create(user_id=user.id, content=content)


def create_post_tag(post=None, tag=None, post_type=PostTypeChoiceEnum.POST):
    if not post:
        post = create_post()
    if not tag:
        tag = create_tag()

    return PostTag.objects.create(post_id=post.id, tag=tag, post_type=post_type)
