# -*- coding: utf-8 -*-
from django.test import TestCase

import mock
from account.testing.mock import create_login_user
from chat.models import PostTypeChoiceEnum
from chat.testing.mock import create_post
from favor.models import Favor


class FavorTest(TestCase):
    """
    收藏测试用例
    python manage.py test favor.FavorTest
    """
    def test_favor(self):
        """
        测试收藏
        python manage.py test favor.FavorTest.test_favor
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        result = client.json_post('/favor/add/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

    def test_un_favor(self):
        """
        测试取消收藏
        python manage.py test favor.FavorTest.test_un_favor
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        favor = mock.create_favor(user=user, post=post)

        result = Favor.objects.filter(id=favor.id, is_deleted=False).exists()
        self.assertEqual(result, True)

        result = client.json_post('/favor/delete/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

        result = Favor.objects.filter(id=favor.id, is_deleted=False).exists()
        self.assertEqual(result, False)
