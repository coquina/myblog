from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(requeset):
    '''
    SHOW'Hello world! in the main page
    :param requeset:
    :return:
    '''
    return HttpResponse('Hello world!')