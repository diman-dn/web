from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')

def qa_list_all(request):
	return HttpResponse('ok')

def login_add(request):
	return HttpResponse('ok')

def signup_add(request):
	return HttpResponse('ok')

def question(request, id):
	return HttpResponse('ok: ' + id)

def ask_add(request):
	return HttpResponse('ok')

def answer_add(request):
	return HttpResponse('ok')

def qa_popular_all(request):
	return HttpResponse('ok')
