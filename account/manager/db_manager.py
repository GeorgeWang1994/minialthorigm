# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from comment.models import PostComment
from favor.models import PostFavor
from chat.models import Post
from article.models import Article


def get_user_by_id(user_id):
    """
    获取用户对象
    :param user_id:
    :return:
    """
    try:
        return User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None


def get_user_comments_qs(user):
    """
    获取用户的评论
    :param user:
    :return:
    """
    return PostComment.objects.filter(author_id=user.id)


def get_user_favors_qs(user):
    """
    获取用户的收藏
    :param user:
    :return:
    """
    return PostFavor.objects.filter(user_id=user.id)


def get_user_create_posts_qs(user):
    """
    获取用户发布的帖子
    :param user:
    :return:
    """
    return Post.objects.filter(author_id=user.id)


def get_user_participate_posts_qs(user):
    return Post.objects.filter()


def get_user_create_articles_qs(user):
    """
    获取用户发布的文章
    :param user:
    :return:
    """
    return Article.objects.filter(author_id=user.id)


def get_user_participate_articles_qs(user):
    return Article.objects.filter()


def get_user_comments_by_type_qs(comments_qs, post_type):
    """
    获取用户的评论qs
    :param comments_qs:
    :param post_type:
    :return:
    """
    return comments_qs.filter(post_type=post_type).order_by('-created_time')


def get_user_favors_by_type_qs(favors_qs, post_type):
    """
    获取用户的收藏qs
    :param favors_qs:
    :param post_type:
    :return:
    """
    return favors_qs.filter(post_type=post_type).order_by('-created_time')


def get_user_comments_count(comments_qs):
    return comments_qs.count()


def get_user_posts_count(posts_qs):
    return posts_qs.count()


def get_user_favors_count(favors_qs):
    return favors_qs.count()
