# -*- coding: utf-8 -*-

import db_manager
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
    if not post:
        return {}

    user = db_manager.get_user_by_id(post.author_id)
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


def build_home_info():
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
    return info


def build_hot_info():
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
    return info
