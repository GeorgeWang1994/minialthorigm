# -*- coding: utf-8 -*-

from comment.models import Comment
from chat.models import PostTypeChoiceEnum
from account.testing.mock import create_user
from chat.testing.mock import create_post


def create_comment(user=None, post=None, post_type=PostTypeChoiceEnum.POST):
    user = user or create_user()
    post = post or create_post(author=user)

    return Comment.objects.create(author_id=user.id, post_id=post.id, post_type=post_type)
