from django.http import HttpResponse


def post(request):
    return HttpResponse("hello world")