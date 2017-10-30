# -*- coding: utf-8 -*-

import mock
from django.test import TestCase
from utils.utils_cls import CustomClient


class UserTest(TestCase):
    """
    测试用户相关信息
    python manage.py test account.UserTest
    """
    def test_detail(self):
        """
        测试用户详细信息
        python manage.py test account.UserTest.test_detail
        """
        client, user = mock.create_login_user()
        user_info = mock.create_user_info(user=user)
        result = client.json_get('/account/%s/detail/' % user.id)

        self.assertEqual(result['username'], user.username)
        self.assertEqual(result['email'], user.email)
        self.assertEqual(result['like_count'], user_info.like_count)
        self.assertEqual(result['comment_count'], user_info.comment_count)
        self.assertEqual(result['favor_count'], user_info.favor_count)
