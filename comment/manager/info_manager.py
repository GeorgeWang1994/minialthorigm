# -*- coding: utf-8 -*-

import db_manager
from chat.manager.db_manager import get_post_by_id


def comment_post(user_id, post_id, post_type):
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

    db_manager.create_post_comment_db(user_id, post_id, post_type)
    return 0, u''


def del_comment_post(user_id, post_id, post_type):
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

    comment = db_manager.get_comment_by_id(user_id, post_id, post_type)
    if not comment:
        return 1, u'没有评论过'

    db_manager.delete_post_comment_db(comment)
    return 0, u''
