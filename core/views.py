from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def json_test(request):
    return JsonResponse({'foo': 'bar'})
