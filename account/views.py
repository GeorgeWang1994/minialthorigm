# -*- coding: utf-8 -*-

from account.manager import db_manager, info_manager
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_view_exempt


@login_required
@csrf_view_exempt
def detail_view(request, user_id):
    user = db_manager.get_user_by_id(user_id)
    return info_manager.build_user_info(user)


@login_required
@csrf_view_exempt
def user_favors_view(request, user_id):
    pass


@login_required
@csrf_view_exempt
def user_comments_view(request, user_id):
    pass
