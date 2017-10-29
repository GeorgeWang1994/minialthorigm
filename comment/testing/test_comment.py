# -*- coding: utf-8 -*-
from django.test import TestCase

import mock
from account.testing.mock import create_login_user
from chat.models import PostTypeChoiceEnum
from chat.testing.mock import create_post
from comment.models import Comment


class CommentTest(TestCase):
    """
    收藏测试用例
    python manage.py test comment.CommentTest
    """
    def test_favor(self):
        """
        测试评论
        python manage.py test comment.CommentTest.test_favor
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        result = client.json_post('/comment/add/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

    def test_un_favor(self):
        """
        测试删除评论
        python manage.py test comment.CommentTest.test_un_favor
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')
        favor = mock.create_comment(user=user, post=post)

        result = Comment.objects.filter(id=favor.id, is_deleted=False).exists()
        self.assertEqual(result, True)

        result = client.json_post('/comment/delete/', {'post_id': post.id, 'post_type': PostTypeChoiceEnum.POST})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

        result = Comment.objects.filter(id=favor.id, is_deleted=False).exists()
        self.assertEqual(result, False)
