# -*- coding: utf-8 -*-

import db_manager
from comment.models import CommentTypeChoiceEnum
from chat.models import PostTypeChoiceEnum
from account.models import UserInfo


def get_post_info_by_qs(post_qs):
    """
    通过qs获取帖子
    :param post_qs:
    :return:
    """
    return post_qs.values('content', 'favor_count', 'comment_count')


def get_article_info_by_qs(article_qs):
    """
    通过qs获取文章
    :param article_qs:
    :return:
    """
    return article_qs.values('title', 'content', 'url', 'favor_count', 'comment_count')


def get_comment_info_by_qs(comment_qs):
    return comment_qs.values('content')


def get_post_and_article_info(post_qs, article_qs):
    """
    获取帖子和文章信息
    :param post_qs:
    :param article_qs:
    :return:
    """
    return {
        'posts': get_post_info_by_qs(post_qs),
        'articles': get_article_info_by_qs(article_qs),
    }


def get_post_and_article_comment_info(post_qs, article_qs, comment_qs):
    """
    获取帖子和文章和评论信息
    :param post_qs:
    :param article_qs:
    :param comment_qs:
    :return:
    """
    return {
        'posts': get_post_info_by_qs(post_qs),
        'articles': get_article_info_by_qs(article_qs),
        'comments': get_comment_info_by_qs(comment_qs),
    }


def build_user_info(user):
    """
    构建用户相关信息
    :param user:
    :return:
    """
    user_info = UserInfo.objects.get(user=user)

    return {
        'username': user.username,
        'email': user.email,
        'like_count': user_info.like_count,
        'comment_count': user_info.comment_count,
        'favor_count': user_info.favor_count,
    }


def build_user_create_posts_and_article_info(user):
    """
    构建用户的创建的帖子和文章信息
    :param user:
    :return:
    """
    post_qs = db_manager.get_user_create_posts_qs(user)
    article_qs = db_manager.get_user_create_articles_qs(user)

    return {
        'posts': get_post_info_by_qs(post_qs),
        'articles': get_article_info_by_qs(article_qs),
    }


def build_user_participate_posts_and_article_info(user):
    """
    构建用户参与的帖子和文章信息
    :param user:
    :return:
    """
    post_qs = db_manager.get_user_participate_posts_qs(user).values('content', 'favor_count', 'comment_count')
    article_qs = db_manager.get_user_participate_articles_qs(user).values('title', 'content', 'url', 'favor_count', 'comment_count')

    return {
        'posts': get_post_info_by_qs(post_qs),
        'articles': get_article_info_by_qs(article_qs),
    }


def build_user_favors_info(user):
    """
    构建用户收藏的信息
    :param user:
    :return:
    """
    favor_qs = db_manager.get_user_favors_qs(user)
    post_favor_qs = db_manager.get_user_favors_qs_by_type(favor_qs, PostTypeChoiceEnum.POST)
    article_favor_qs = db_manager.get_user_favors_qs_by_type(favor_qs, PostTypeChoiceEnum.ARTICLE)

    post_qs = db_manager.get_user_post_qs_by_favor_or_like_or_comment_qs(post_favor_qs)
    article_qs = db_manager.get_user_article_qs_by_favor_or_like_or_comment_qs(article_favor_qs)

    return get_post_and_article_info(post_qs, article_qs)


def build_user_comments_info(user):
    """
    构建用户评论的信息
    :param user:
    :return:
    """
    comment_qs = db_manager.get_user_comments_qs(user)
    post_comment_qs = db_manager.get_user_favors_qs_by_type(comment_qs, CommentTypeChoiceEnum.POST)
    article_comment_qs = db_manager.get_user_favors_qs_by_type(comment_qs, CommentTypeChoiceEnum.ARTICLE)

    post_qs = db_manager.get_user_post_qs_by_favor_or_like_or_comment_qs(post_comment_qs)
    article_qs = db_manager.get_user_article_qs_by_favor_or_like_or_comment_qs(article_comment_qs)

    return get_post_and_article_info(post_qs, article_qs)


def build_user_likes_info(user):
    """
    构建用户点赞信息
    :param user:
    :return:
    """
    like_qs = db_manager.get_user_comments_qs(user)
    post_like_qs = db_manager.get_user_likes_qs_by_type(like_qs, CommentTypeChoiceEnum.POST)
    article_like_qs = db_manager.get_user_likes_qs_by_type(like_qs, CommentTypeChoiceEnum.ARTICLE)

    post_qs = db_manager.get_user_post_qs_by_favor_or_like_or_comment_qs(post_like_qs)
    article_qs = db_manager.get_user_article_qs_by_favor_or_like_or_comment_qs(article_like_qs)

    return get_post_and_article_info(post_qs, article_qs)
