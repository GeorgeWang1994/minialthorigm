# -*- coding: utf-8 -*-

from django.test import TestCase
from chat.testing.mock import create_post
from utils.utils_cls import CustomClient
from account.testing.mock import create_login_user


class ChatTest(TestCase):
    """
    聊天测试用例
    python manage.py test chat.ChatTest
    """
    def test_home_view(self):
        """
        测试主页
        python manage.py test chat.ChatTest.test_home_view
        """
        post = create_post(content='这是我的帖子')
        client = CustomClient()
        result = client.json_get("/chat/last/list/")
        self.assertEqual(result["posts"][0]['content'], post.content)

    def test_hot_view(self):
        """
        测试热门
        python manage.py test chat.ChatTest.test_hot_view
        """
        post = create_post(content='这是我的帖子')
        client = CustomClient()
        result = client.json_get("/chat/hot/list/")
        self.assertEqual(result["posts"][0]['content'], post.content)

    def test_create_post_view(self):
        """
        测试创建post
        python manage.py test chat.ChatTest.test_create_post_view
        """
        client, user = create_login_user()
        result = client.json_post('/chat/create/', {'content': u'帖子的内容'})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')

    def test_get_post_view(self):
        """
        测试获取post
        python manage.py test chat.ChatTest.test_get_post_view
        """
        client, user = create_login_user()
        post = create_post(content='这是我的帖子')

        result = client.json_get('/chat/%s/detail/' % post.id)
        self.assertEqual(result['id'], post.id)
        self.assertEqual(result['content'], post.content)

    def test_del_post_view(self):
        """
        测试删除post
        python manage.py test chat.ChatTest.test_del_post_view
        """
        client, user = create_login_user()
        post = create_post(author=user, content='这是我的帖子')

        result = client.json_post('/chat/delete/', {'post_id': post.id})
        self.assertEqual(result['error'], 0)
        self.assertEqual(result['error_msg'], u'')
