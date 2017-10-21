# -*- coding: utf-8 -*-

from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=300, help_text=u'帖子内容')
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    favor_count = models.IntegerField(default=0, help_text=u'帖子点赞个数')
    comment_count = models.IntegerField(default=0, help_text=u'帖子评论个数')
    create_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')


class PostComment(models.Model):
    content = models.CharField(max_length=300, help_text=u'评论内容')
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    comment_post = models.ForeignKey(Post, help_text=u'评论文章')
    create_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')


class PostFavor(models.Model):
    author_id = models.CharField(max_length=20, unique=True, help_text=u'用户id')
    favor_post = models.ForeignKey(Post, help_text=u'喜欢的文章')
    create_time = models.DateTimeField(auto_now_add=True, help_text=u'创建时间')
