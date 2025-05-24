from django.http import HttpResponse

def index(request):
    return HttpResponse("اولین صفحه‌ی من")

