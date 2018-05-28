from django.shortcuts import render
from datetime import datetime
# Create your views here.

def main(request):
    '''
    Render the main page
    :param requeset:
    :return:
    '''
    like = 'Django好棒'
    time = datetime.now()
    return render(request, 'main/main.html', locals())
# def time(request):
#     '''
#
#     :param request:
#     :return:
#     '''
#     noontime = datetime.now().strptime('12:0:0')
#     now = datetime.now().strftime('%H:%M:%S')
#     if now > str(noontime):
#         show = '午安'
#         return render(request, 'main/main.html', locals())
#     else:
#         show1 = '早安'
#         return render(request, 'main/main.html', locals())



def about(request):
    '''
    Render the about page
    :param request:
    :return:
    '''
    return render(request, 'main/about.html' )