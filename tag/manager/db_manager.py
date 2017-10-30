# -*- coding: utf-8 -*-

from tag.models import Tag, PostTag


def get_tag_by_id(tag_id):
    try:
        return Tag.objects.get(id=tag_id, is_deleted=False)
    except Tag.DoesNotExist:
        return None


def get_post_tag_by_id(tag, post, post_type):
    try:
        return PostTag.objects.get(tag=tag, post_id=post.id, post_type=post_type, is_deleted=False)
    except PostTag.DoesNotExist:
        return None


def create_tag_db(user_id, content):
    """
    创建标签
    :param user_id:
    :param content:
    :return:
    """
    return Tag.objects.get_or_create(user_id=user_id, content=content, is_deleted=False)


def create_post_tag_db(tag, post, post_type):
    """
    为文章添加标签
    :param tag:
    :param post:
    :param post_type:
    :return:
    """
    return PostTag.objects.get_or_create(tag=tag, post_id=post.id, post_type=post_type, is_deleted=False)


def delete_post_tag_db(post_tag):
    """
    删除文章标签
    :param post_tag:
    :return:
    """
    post_tag.is_deleted = True
    post_tag.save()