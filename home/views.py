from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'variable' : "this is set",
        'variable2' : "Sahaj is great"
    }
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):
    # return HttpResponse("This is services page")
    return render(request, 'Services.html')

def contact(request):
    # return HttpResponse("This is contact page")
    return render(request, 'Contact.html')