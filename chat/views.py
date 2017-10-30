# -*- coding: utf-8 -*-

from django.views.decorators.csrf import csrf_view_exempt
from django.contrib.auth.decorators import login_required

from manager import info_manager
from manager import db_manager
from utils.utils_func import author, json_http_response, get_user_by_request


@author(author_name='George1994')
@csrf_view_exempt
def home_view(request):
    home_info = info_manager.get_home_posts()
    return json_http_response(home_info)


@author(author_name='George1994')
@csrf_view_exempt
def hot_post_view(request):
    hot_info = info_manager.get_hot_posts()
    return json_http_response(hot_info)


@author(author_name='George1994')
@csrf_view_exempt
def get_post_view(request, post_id):
    info = info_manager.get_post(post_id)
    return json_http_response(info)


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def create_post_view(request):
    content = request.POST['content']
    user = get_user_by_request(request)

    db_manager.create_post_db(content=content, author_id=user.id)
    return json_http_response({'error': 0, 'error_msg': u''})


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def del_post_view(request):
    post_id = request.POST['post_id']
    user = get_user_by_request(request)

    error, msg = info_manager.delete_post(user.id, post_id)
    return json_http_response({'error': error, 'error_msg': msg})
