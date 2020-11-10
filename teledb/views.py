from django.http import HttpResponse


def teledb(res, par):
    return HttpResponse(par)


def username(res, uname):
    return HttpResponse()
