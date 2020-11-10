from django.http import HttpResponse


def home(res):
    return HttpResponse('Hello World!')
