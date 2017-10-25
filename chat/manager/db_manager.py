# -*- coding: utf-8 -*-

from chat.models import Post


def get_post_by_id(post_id):
    try:
        return Post.objects.get(id=post_id)
    except Post.DoesNotExist:
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
    return get_valid_post_qs().order_by('-created_time', '-favor_count', '-comment_count')


def get_hot_qs():
    """
    根据评论数来对帖子进行排序
    :return:
    """
    return get_valid_post_qs().order_by('-comment_count', '-favor_count', '-created_time')


def create_post_db(content, author_id):
    """
    创建帖子
    :param content:
    :param author_id:
    :return:
    """
    return Post.objects.create(content=content, author_id=author_id)


def del_post_db(post):
    """
    删除post
    :param post:
    :return:
    """
    post.delete()


def can_modify_post(post, user_id):
    """
    判断是否拥有更改post的权限
    :param post:
    :param user_id:
    :return:
    """
    if not post:
        return 1, u'不存在该帖子'

    if post.author_id != user_id:
        return 1, u'没有权限'

    return 0, u''
