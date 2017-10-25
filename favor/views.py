# Create your views here.

from django.views.decorators.csrf import csrf_view_exempt
from django.contrib.auth.decorators import login_required

from manager import info_manager
from utils.utils_func import author, json_http_response, get_user_by_request


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def favor_post_view(request):
    post_id = request.POST['post_id']
    user = get_user_by_request(request)

    error, msg = info_manager.favor_post(user.id, post_id)
    return json_http_response({'error': error, 'msg': msg})


@author(author_name='George1994')
@login_required
@csrf_view_exempt
def un_favor_post_view(request):
    post_id = request.POST['post_id']
    user = get_user_by_request(request)

    error, msg = info_manager.un_favor_post(user.id, post_id)
    return {'error': error, 'msg': msg}
