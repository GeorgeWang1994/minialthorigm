# -*- coding: utf-8 -*-

from comment.models import Comment


def get_comment_by_id(user_id, post_id, post_type):
    try:
        return Comment.objects.get(author_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)
    except Comment.DoesNotExist:
        return None


def create_post_comment_db(user_id, post_id, post_type):
    """
    评论
    :param user_id:
    :param post_id:
    :param post_type:
    :return:
    """
    return Comment.objects.get_or_create(author_id=user_id, post_id=post_id, post_type=post_type, is_deleted=False)


def delete_post_comment_db(comment):
    """
    删除评论
    :param comment:
    :return:
    """
    comment.is_deleted = True
    comment.save()
