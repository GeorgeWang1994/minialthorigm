# -*- coding: utf-8 -*-

import importlib
import inspect
import json
import random
import string

import fnmatch
import os
from django.http import HttpResponse
from django.test import TestCase

from minialgorithm.settings import BASE_DIR


def find_files_recursively(root_path, filename='*', prefix='', suffix='.py', exclude_name=()):
    """
    递归的查找文件
    :param root_path: 文件路径
    :param filename: 需要搜索的文件名
    :param prefix: 文件名前缀
    :param suffix: 文件名后缀
    :param exclude_name: 去除的文件名
    :return: 搜索出的文件
    """
    matches = {}
    for root, dir_names, file_names in os.walk(root_path):
        for name in fnmatch.filter(file_names, prefix + filename + suffix):
            if name in exclude_name:
                continue
            matches[name] = os.path.join(root, name)

    return matches


def add_app_testcase(app_name):
    """
    获取当前app下testing文件夹中的所有测试用例
    :return:
    """
    app_dir = os.path.join(BASE_DIR, app_name)
    if not os.path.exists(app_dir):
        print u'不存在app{0}的路径'.format(app_name)
        return

    testing_dir = os.path.join(app_dir, 'testing')
    if not os.path.exists(testing_dir):
        print u'{0}不存在testing文件夹'.format(app_name)
        return

    # def match_regex(string):
    #     """
    #     正则匹配
    #     :param string:
    #     :return: 匹配结果
    #     """
    #     return re.findall(r"^class (\w+)\((\w+TestCase\w+)\):", string, flags=re.MULTILINE)

    matches = find_files_recursively(testing_dir, exclude_name=('__init__.py', 'mock.py'))
    test_cases = {}

    for file_name, file_path in matches.items():
        if file_name[:4] != 'test':
            continue

        file_module = importlib.import_module('{0}.testing.{1}'.format(app_name, file_name[:-3]))
        for name, obj in inspect.getmembers(file_module):
            if not inspect.isclass(obj):
                continue

            if issubclass(obj, TestCase):
                test_cases[name] = obj

    return test_cases


def author(author_name='George1994'):
    """
    作者装饰器
    :param author_name: 作者名字
    :return:
    """
    def _decor(func):
        func.author_name = author_name
        return func
    return _decor


def str_time_format(time, str_format="%Y-%m-%d"):
    """
    将时间转化为固定格式的字符串
    :param time: 时间
    :param str_format: 格式
    :return:
    """
    return time.strftime(str_format)


def json_http_response(content):
    """
    将内容序列化后以response的形式返回
    :param content: 字典的内容
    :return:
    """
    return HttpResponse(content=json.dumps(content), mimetype="application/json; charset=UTF-8",
                        status=200)


def random_str(num=12):
    """
    生成指定个数的随机字符串
    :param num: 个数
    :return:
    """
    return "".join(random.sample(string.ascii_letters + string.digits, num))


def random_num(start=-100000, end=100000):
    """
    生成指定范围的随机数字
    :param start: 起始
    :param end: 结束
    :return:
    """
    return random.randint(start, end)


def get_user_by_request(request):
    return request.user
