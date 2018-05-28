from django.shortcuts import render

# Create your views here.

def main(request):
    '''
    Render the main page
    :param requeset:
    :return:
    '''
    context={'like': 'Django 很棒'}
    return render(request, 'main/main.html', context)
def about(request):
    '''
    Render the about page
    :param request:
    :return:
    '''
    return render(request, 'main/about.html' )