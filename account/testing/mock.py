# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from utils.utils_func import random_str
from utils.utils_cls import CustomClient


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
    client.login(username=user.username, email=user.email, password=user.password)
    return client, user


def logout_user(client, user):
    """
    用户退出登陆
    :param client: 客户端
    :param user: 用户
    :return:
    """
    client.logout(user)


def create_user(username='', email='', password=''):
    username = username or random_str()
    email = email or random_str()
    password = password or random_str()

    return User.objects.create_user(username=username, email=email, password=password)
