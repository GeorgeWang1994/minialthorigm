# -*- coding: utf-8 -*-

from django.test import TestCase
from chat.testing.mock import create_post
from utils.utils_cls import CustomClient


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
