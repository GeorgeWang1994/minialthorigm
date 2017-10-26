# -*- coding: utf-8 -*-

from like.models import Like


def get_like_by_id(user_id, post_id, post_type):
    try:
        return Like.objects.get(user_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)
    except Like.DoesNotExist:
        return None


def create_like_post_db(user_id, post_id, post_type):
    """
    点赞
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    return Like.objects.get_or_create(user_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)


def delete_like_post_db(like):
    """
    取消点赞
    :param like:
    :return:
    """
    like.is_deleted = True
    like.save()