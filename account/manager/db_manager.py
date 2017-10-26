# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from article.models import Article
from chat.models import Post
from comment.models import Comment, CommentTypeChoiceEnum
from favor.models import Favor
from like.models import Like


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
    获取用户的评论qs
    :param user:
    :return:
    """
    return Comment.objects.filter(author_id=user.id)


def get_user_favors_qs(user):
    """
    获取用户的收藏qs
    :param user:
    :return:
    """
    return Favor.objects.filter(user_id=user.id)


def get_user_likes_qs(user):
    """
    获取用户的点赞qs
    :param user:
    :return:
    """
    return Like.objects.filter(user_id=user.id)


def get_user_create_posts_qs(user):
    """
    获取用户发布的帖子
    :param user:
    :return:
    """
    return Post.objects.filter(author_id=user.id)


def get_user_participate_posts_qs(user):
    """
    获取用户参与的帖子，包括对帖子进行点赞、评论
    :param user:
    :return:
    """
    like_post_ids = get_user_likes_ids_by_type(user.id, LikeTypeChoiceEnum.POST)
    comment_post_ids = Comment.objects.filter(user.id, CommentTypeChoiceEnum.POST)

    return Post.objects.filter(id__=set(like_post_ids + comment_post_ids))


def get_user_create_articles_qs(user):
    """
    获取用户发布的文章
    :param user:
    :return:
    """
    return Article.objects.filter(author_id=user.id)


def get_user_participate_articles_qs(user):
    """
    获取用户参与的文章，包括对文章进行点赞、评论
    :param user:
    :return:
    """
    like_article_ids = get_user_likes_ids_by_type(user.id, LikeTypeChoiceEnum.ARTICLE)
    comment_article_ids = Comment.objects.filter(user.id, CommentTypeChoiceEnum.ARTICLE)

    return Article.objects.filter(id__in=set(like_article_ids + comment_article_ids))


def get_user_comments_qs_by_type(comment_qs, post_type):
    """
    获取用户的评论qs
    :param comment_qs:
    :param post_type:
    :return:
    """
    return comment_qs.filter(post_type=post_type).order_by('-created_time')


def get_user_likes_ids_by_type(user_id, post_type):
    """
    通过类型来获取用户点赞过的id
    :param user_id:
    :param post_type:
    :return:
    """
    return Like.objects.filter(user_id=user_id, type=post_type).values_list('post_id')


def get_user_likes_qs_by_type(like_qs, post_type):
    """
    获取用户的点赞qs
    :param like_qs:
    :param post_type:
    :return:
    """
    return like_qs.filter(post_type=post_type).order_by('-created_time')


def get_user_favors_qs_by_type(favor_qs, post_type):
    """
    获取用户的收藏qs
    :param favor_qs:
    :param post_type:
    :return:
    """
    return favor_qs.filter(post_type=post_type).order_by('-created_time')


def get_user_post_qs_by_favor_or_like_or_comment_qs(favor_or_like_or_comment_qs):
    """
    通过收藏qs来获取帖子qs
    :param favor_or_like_or_comment_qs:
    :return:
    """
    return Post.objects.filter(id__in=[instance.post_id for instance in favor_or_like_or_comment_qs])


def get_user_article_qs_by_favor_or_like_or_comment_qs(favor_or_like_or_comment_qs):
    """
    通过收藏qs来获取文章qs
    :param favor_or_like_or_comment_qs:
    :return:
    """
    return Article.objects.filter(id__in=[instance.post_id for instance in favor_or_like_or_comment_qs])


def get_user_comments_count_by_qs(comments_qs):
    """
    通过qs获取用户评论的个数
    :param comments_qs:
    :return:
    """
    return comments_qs.count()


def get_user_likes_count_by_qs(like_qs):
    """
    通过qs获取用户点赞的个数
    :param like_qs:
    :return:
    """
    return like_qs.count()


def get_user_posts_count_by_qs(post_qs):
    """
    通过qs获取文章的个数
    :param post_qs:
    :return:
    """
    return post_qs.count()


def get_user_favors_count_by_qs(favor_qs):
    """
    通过qs获取收藏的个数
    :param favor_qs:
    :return:
    """
    return favor_qs.count()
