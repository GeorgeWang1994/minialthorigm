# -*- coding: utf-8 -*-
from django.test import TestCase

import mock
from account.testing.mock import create_login_user
from chat.testing.mock import create_post
from chat.models import PostTypeChoiceEnum
from like.models import Like


class LikeTest(TestCase):
    """
    收藏测试用例
    python manage.py test like.LikeTest
    """
    def test_like(self):
        """
        测试收藏
        python manage.py test like.LikeTest.test_like
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        result = client.json_post('/like/add/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

    def test_un_like(self):
        """
        测试取消收藏
        python manage.py test like.LikeTest.test_un_like
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        like = mock.create_like(user=user, post=post)

        result = Like.objects.filter(id=like.id, is_deleted=False).exists()
        self.assertEqual(result, True)

        result = client.json_post('/like/delete/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

        result = Like.objects.filter(id=like.id, is_deleted=False).exists()
        self.assertEqual(result, False)
