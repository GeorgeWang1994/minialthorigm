# Create your views here.

from django.views.decorators.csrf import csrf_view_exempt
from django.contrib.auth.decorators import login_required

from manager import info_manager
from utils.utils_func import author, json_http_response, get_user_by_request


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def add_comment_post_view(request):
    post_id = request.POST['post_id']
    post_type = request.POST['post_type']
    user = get_user_by_request(request)

    error, msg = info_manager.comment_post(user.id, post_id, post_type)
    return json_http_response({'error': error, 'error_msg': msg})


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def del_comment_post_view(request):
    post_id = request.POST['post_id']
    post_type = request.POST['post_type']
    user = get_user_by_request(request)

    error, msg = info_manager.del_comment_post(user.id, post_id, post_type)
    return json_http_response({'error': error, 'error_msg': msg})
