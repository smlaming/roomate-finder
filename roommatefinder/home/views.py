# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Our roommate finder page ^_^")
