# -*- coding: utf-8 -*-

import db_manager
from account.manager.db_manager import get_user_by_id
from utils.utils_func import str_time_format


def build_one_post_info(post):
    """
    构建一篇帖子的返回信息
    :param post: 帖子
    :return:
    {
        id: "123456",
        content: "发言",
        author:
        {
            id: "455656",
            name: "ming",
        }
        favor_count: 0,
        comment_count: 0,
        create_time: "2017-10-09",
    }
    """
    user = get_user_by_id(post.author_id)
    return {
        'id': post.id,
        'content': post.content,
        'author': {
            'id': user.id,
            'name': user.username,
        },
        'favor_count': post.favor_count,
        'comment_count': post.comment_count,
        'create_time': str_time_format(post.created_time),
    }


def get_home_posts():
    """
    构建主页帖子的返回信息
    :return:
    {
        [
            {
                id: "123456",
                content: "发言",
                author:
                {
                    id: "455656",
                    name: "ming",
                }
                favor_count: 0,
                comment_count: 0,
                create_time: "2017-10-09",
            }
        ]
    }
    """
    home_qs = db_manager.get_home_qs()
    info = []

    for qs in home_qs:
        info.append(build_one_post_info(qs))
    return {"posts": info}


def get_hot_posts():
    """
        构建热门帖子的返回信息
        :return:
        {
            [
                {
                    id: "123456",
                    content: "发言",
                    author:
                    {
                        id: "455656",
                        name: "ming",
                    }
                    favor_count: 0,
                    comment_count: 0,
                    create_time: "2017-10-09",
                }
            ]
        }
        """
    hot_qs = db_manager.get_hot_qs()
    info = []

    for qs in hot_qs:
        info.append(build_one_post_info(qs))
    return {"posts": info}


def delete_post(user_id, post_id):
    """
    删除帖子
    注意：需不需要把相关的模型也删除？
    :param user_id:
    :param post_id:
    :return:
    """
    post = db_manager.get_post_by_id(post_id)
    if not post:
        return 1, u'不存在该帖子'
    if post.author_id != user_id:
        return 1, u'没有权限'

    db_manager.del_post_db(post)
    return 0, u''


def get_post(post_id):
    """
    获取帖子相关信息
    :param post_id:
    :return:
    """
    post = db_manager.get_post_by_id(post_id)
    return build_one_post_info(post)
