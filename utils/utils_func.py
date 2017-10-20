# -*- coding: utf-8 -*-

import importlib
import inspect

import fnmatch
import os
from django.test import TestCase

from settings import PROJECT_DIR


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
    app_dir = os.path.join(PROJECT_DIR, app_name)
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

    matches = find_files_recursively(testing_dir, exclude_name=('__init__.py', ))
    test_cases = {}

    for file_name, file_path in matches.items():
        file_module = importlib.import_module('{0}.testing.{1}'.format(app_name, file_name[:-3]))
        for name, obj in inspect.getmembers(file_module):
            if not inspect.isclass(obj):
                continue

            if issubclass(obj, TestCase):
                test_cases[name] = obj

    return test_cases
