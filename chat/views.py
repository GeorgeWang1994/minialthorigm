# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_view_exempt

from manager import info_manager
from utils.utils_func import author, json_http_response


@author(author_name='George1994')
@csrf_view_exempt
def home_view(request):
    home_info = info_manager.build_home_info()
    return json_http_response({"posts": home_info})


@author(author_name='George1994')
@csrf_view_exempt
def hot_post_view(request):
    hot_info = info_manager.build_hot_info()
    return json_http_response({"posts": hot_info})


def create_post_view():
    pass


def update_post_view():
    pass


def del_post_view():
    pass


def like_post_view():
    pass


def unlike_post_view():
    pass


def comment_post_view():
    pass


def get_post_view():
    pass
