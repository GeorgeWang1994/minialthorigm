# -*- coding: utf-8 -*-

import db_manager
from chat.models import PostTypeChoiceEnum


def build_user_info(user):
    """
    构建用户相关信息
    :param user:
    :return:
    """
    comments_qs = db_manager.get_user_comments_qs(user)
    favors_qs = db_manager.get_user_favors_qs(user)

    return {
        'username': user.username,
        'email': user.email,
        'comments_count': db_manager.get_user_comments_count(comments_qs),
        'favors_count': db_manager.get_user_favors_count(favors_qs),
    }


def build_user_create_posts_and_article_info(user):
    """
    构建用户的创建的帖子和文章信息
    :param user:
    :return:
    """
    posts_info = db_manager.get_user_create_posts_qs(user).values('content', 'favor_count', 'comment_count')
    article_info = db_manager.get_user_create_articles_qs(user).values('title', 'content', 'url', 'favor_count', 'comment_count')

    return {
        'posts': posts_info,
        'articles': article_info,
    }


def build_user_participate_posts_and_article_info(user):
    """
    构建用户参与的帖子和文章信息
    :param user:
    :return:
    """
    pass
