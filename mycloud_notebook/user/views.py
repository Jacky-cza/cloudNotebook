from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
from . import models

def mylogin(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    elif request.method == 'POST':
        # 获取表单的数据
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        # 验证用户名，密码是否正确
        try:
            user = models.User.objects.get(name=username,password=password)
            # 在当前连接的Session中记录当前用户的信息
            request.session['userinfo'] = {
                "username": user.name,
                'id': user.id
            }
            return HttpResponseRedirect('/')  # 回到首页
        except:
            return HttpResponse("登陆失败")



def mylogout(request):
    '退出登陆'
    if 'userinfo' in request.session:
        del request.session['userinfo']
    return HttpResponseRedirect('/')  # 注销后跳转到主页



