# -*- coding: utf-8 -*-

import db_manager
from chat.manager.db_manager import get_post_by_id


def like_post(user_id, post_id, post_type):
    """
    点赞帖子
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    like, created = db_manager.create_like_post_db(user_id, post_id, post_type)
    if not created:
        return 1, u'已经点赞'

    return 0, u''


def un_like_post(user_id, post_id, post_type):
    """
    取消点赞
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    like = db_manager.get_like_by_id(user_id, post_id, post_type)
    if not like:
        return 1, u'没有点赞过'

    db_manager.delete_like_post_db(like)
    return 0, u''
