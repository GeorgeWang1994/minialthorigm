# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_view_exempt

from account.manager import info_manager
from utils.utils_func import get_user_by_request, json_http_response


@login_required
@csrf_view_exempt
def user_detail_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_info(user)
    return json_http_response(info)


@login_required
@csrf_view_exempt
def user_create_posts_and_articles_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_create_posts_and_article_info(user)
    return json_http_response(info)


@login_required
@csrf_view_exempt
def user_participate_posts_and_articles_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_participate_posts_and_article_info(user)
    return json_http_response(info)


@login_required
@csrf_view_exempt
def user_favors_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_favors_info(user)
    return json_http_response(info)


@login_required
@csrf_view_exempt
def user_likes_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_likes_info(user)
    return json_http_response(info)


@login_required
@csrf_view_exempt
def user_comments_view(request):
    user = get_user_by_request(request)
    info = info_manager.build_user_comments_info(user)
    return json_http_response(info)
