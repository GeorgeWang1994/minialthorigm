# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from chat.models import Post


def get_user_by_id(user_id):
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


def get_valid_post_qs():
    """
    获取有效的帖子
    :return:
    """
    return Post.objects.filter(is_deleted=False)


def get_home_qs():
    """
    根据时间来对帖子进行排序
    :return:
    """
    return get_valid_post_qs().order_by('-created_time', '-like_count', '-comment_count')


def get_hot_qs():
    """
    根据评论数来对帖子进行排序
    :return:
    """
    return get_valid_post_qs().order_by('-comment_count', '-like_count', '-created_time')
