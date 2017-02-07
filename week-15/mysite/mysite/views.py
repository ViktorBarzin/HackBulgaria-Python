from django.http import HttpResponse
from django.shortcuts import render
from mysite.helpers.helpers import fact, fib, get_first_n_primes, run_length_encode, run_lenght_decode


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


def prime_calc(request):
    input_number = int(request.POST.dict().get('number'))
    prime_result = ','.join([str(x) for x in get_first_n_primes(input_number)])
    return render(request, 'index.html', locals())


def encode_rle(request):
    inp = request.POST.dict().get('text')
    encoded = run_length_encode(inp)
    return render(request, 'index.html', locals())


def decode_rle(request):
    inp = request.POST.dict().get('text')
    decoded = run_lenght_decode(inp)
    return render(request, 'index.html', locals())

def not_found(request):
    return HttpResponse('Nqma takava stranica moi!')
