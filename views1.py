from django.http import HttpResponse
def index1(request):
    return HttpResponse("Home")
def about(request):
    return HttpResponse("remove punc")
def capfirst(request):
    return HttpResponse("capitalize first")