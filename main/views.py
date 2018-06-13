from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.urls.base import reverse
# Create your views here.

def main(request):
    '''
    Render the main page
    :param requeset:
    :return:
    '''

    time = datetime.now()
    return render(request, 'main/main.html', locals())



def about(request):
    '''
    Render the about page
    :param request:
    :return:
    '''
    return render(request, 'main/about.html' )

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, ' 請以管理者身份登入')
            return redirect(reverse('account:login')+ '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth