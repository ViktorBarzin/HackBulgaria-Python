from django.http import HttpResponse
from django.shortcuts import render
from mysite.helpers.helpers import fact, fib


def index(request):
    return render(request, 'index.html', locals())


def factorial(request):
    # import ipdb; ipdb.set_trace()

    input_number = int(request.POST.dict().get('number'))
    factorial_result = fact(input_number)
    return render(request, 'index.html', locals())


def fibonacci(request):
    input_number = int(request.POST.dict().get('number'))
    fib_result = fib(input_number)
    return render(request, 'index.html', locals())


def not_found(request):
    return HttpResponse('Nqma takava stranica moi!')
