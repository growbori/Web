from django.shortcuts import render

# Create your views here.

def index(request, num1, num2):
    result = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : result,
    }
    return render(request, 'articles/index.html', context)