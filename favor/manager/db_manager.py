# -*- coding: utf-8 -*-

from favor.models import Favor


def get_favor_by_id(user_id, post_id, post_type):
    try:
        return Favor.objects.get(user_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)
    except Favor.DoesNotExist:
        return None


def create_favor_post_db(user_id, post_id, post_type):
    """
    收藏帖子
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    return Favor.objects.get_or_create(user_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)


def delete_favor_post_db(favor):
    """
    取消收藏帖子
    :param favor:
    :return:
    """
    favor.is_deleted = True
    favor.save()
