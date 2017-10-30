# -*- coding: utf-8 -*-

import db_manager
from chat.manager.db_manager import get_post_by_id


def create_tag(user, content):
    """
    创建标签
    :param user:
    :param content:
    :return:
    """
    db_manager.create_tag_db(user_id=user.id, content=content)
    return 0, u''


def create_post_tag(tag_id, post_id, post_type):
    """
    创建帖子的标签
    :param tag_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    tag = db_manager.get_tag_by_id(tag_id)
    if not tag:
        return 1, u'不存在该标签'

    post_tag, created = db_manager.create_post_tag_db(tag, post, post_type)
    if not created:
        return 1, u'已经创建'

    return 0, u''


def delete_post_tag(tag_id, post_id, post_type):
    """
    删除帖子的标签
    :param tag_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    tag = db_manager.get_tag_by_id(tag_id)
    if not tag:
        return 1, u'不存在该标签'

    post_tag = db_manager.get_post_tag_by_id(tag_id, post, post_type)
    if not post_tag:
        return 1, u'没有为该文章创建过该标签'

    db_manager.delete_post_tag_db(post_tag)
    return 0, u''
