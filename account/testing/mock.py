# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from account.models import UserInfo
from utils.utils_func import random_str
from utils.utils_cls import CustomClient


def create_user(username='', email='', password=''):
    username = username or random_str()
    email = email or random_str()
    password = password or random_str()

    user = User.objects.create_user(username=username, email=email, password=password)
    user.raw_password = password
    return user


def create_user_info(user=None, comment_count=0, favor_count=0, like_count=0):
    if not user:
        user = create_user()

    return UserInfo.objects.create(user=user, comment_count=comment_count,
                                   favor_count=favor_count, like_count=like_count)


def create_client_user():
    """
    生成client和随机的用户
    :return:
    """
    client = CustomClient()
    user = create_user()
    return client, user


def create_login_user(user=None):
    """
    生成登陆的user
    :param user: 用户
    :return:
    """
    client = CustomClient()
    user = user or create_user()
    client.login(username=user.username, password=user.raw_password)
    return client, user


def logout_user(client, user):
    """
    用户退出登陆
    :param client: 客户端
    :param user: 用户
    :return:
    """
    client.logout(user)
