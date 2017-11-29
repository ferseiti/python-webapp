from django.shortcuts import render, HttpResponse

def index(request):
    something = 'Fernando Furusato'

    arguments = { 'myName': something,
                  'age': 32 }
    return render(request, 'containers/test.html', arguments)
    
    #return HttpResponse("Hello, world. You're at the containers index.")
