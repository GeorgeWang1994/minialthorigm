# -*- coding: utf-8 -*-

from chat.models import Post
from account.testing.mock import create_user


def create_post(author=None, content='', comment_count=0, like_count=0):
    author = author or create_user()

    return Post.objects.create(content=content or '内容',
                               author_id=author.id,
                               comment_count=comment_count,
                               like_count=like_count)
