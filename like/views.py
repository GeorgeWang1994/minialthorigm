# Create your views here.

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_view_exempt

from manager import info_manager
from utils.utils_func import author, json_http_response, get_user_by_request


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def like_post_view(request):
    post_id = request.POST['post_id']
    post_type = request.POST['post_type']
    user = get_user_by_request(request)

    error, msg = info_manager.like_post(user.id, post_id, post_type)
    return json_http_response({'error': error, 'error_msg': msg})


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def un_like_post_view(request):
    post_id = request.POST['post_id']
    post_type = request.POST['post_type']
    user = get_user_by_request(request)

    error, msg = info_manager.un_like_post(user.id, post_id, post_type)
    return json_http_response({'error': error, 'error_msg': msg})