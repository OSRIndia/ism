'''
Created on 25-Jul-2012
@author: omi
'''
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to ISM System ")