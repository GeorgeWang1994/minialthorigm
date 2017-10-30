# -*- coding: utf-8 -*-
from django.test import TestCase

import mock
from account.testing.mock import create_login_user
from chat.models import PostTypeChoiceEnum
from chat.testing.mock import create_post
from tag.models import PostTag


class TagTest(TestCase):
    """
    标签测试用例
    python manage.py test tag.TagTest
    """
    def test_create_post_tag(self):
        """
        测试添加标签
        python manage.py test tag.TagTest.test_create_post_tag
        """
        client, user = create_login_user()
        post = create_post(author=user, content=u'这是我的帖子')
        tag = mock.create_tag(user=user, content=u'第一个帖子')
        result = client.json_post('/tag/post/add/', {'tag_id': tag.id, 'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

    def test_del_post_tag(self):
        """
        测试取消添加标签
        python manage.py test tag.TagTest.test_del_post_tag
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        tag = mock.create_tag(user=user, content=u'第一个帖子')

        post_tag = mock.create_post_tag(tag=tag, post=post)

        result = PostTag.objects.filter(id=post_tag.id, is_deleted=False).exists()
        self.assertEqual(result, True)

        result = client.json_post('/tag/post/delete/', {'tag_id': tag.id, 'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

        result = PostTag.objects.filter(id=post_tag.id, is_deleted=False).exists()
        self.assertEqual(result, False)
