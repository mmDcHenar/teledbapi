from django.http import HttpResponse, JsonResponse
from .Search import Search


def teledb(res, par):
    return HttpResponse(par)


def username(res, uname):
    return JsonResponse(Search(uname))


def userid(res, uid):
    return JsonResponse(Search(uid))
