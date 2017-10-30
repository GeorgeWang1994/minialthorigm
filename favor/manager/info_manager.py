# -*- coding: utf-8 -*-

import db_manager
from chat.manager.db_manager import get_post_by_id


def favor_post(user_id, post_id, post_type):
    """
    收藏帖子
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    favor, created = db_manager.create_favor_post_db(user_id, post_id, post_type)
    if not created:
        return 1, u'已经收藏'

    return 0, u''


def un_favor_post(user_id, post_id, post_type):
    """
    取消收藏
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    post = get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'

    favor = db_manager.get_favor_by_id(user_id, post_id, post_type)
    if not favor:
        return 1, u'没有收藏过'

    db_manager.delete_favor_post_db(favor)
    return 0, u''
