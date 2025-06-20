from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "sample_variable": "this is a sample varaible kinda like f string in python"
    }
    return render(request, "index.html", context)
    # return HttpResponse("hello this is home page")

def about(request):
    context = {
        "sample_variable": "this is a sample varaible kinda like f string in python"
    }
    return render(request, "about.html", context)
    # return HttpResponse("hello this is about page")

def menu(request):
    context = {
        "sample_variable": "this is a sample varaible kinda like f string in python"
    }
    return render(request, "menu.html", context)
    # return HttpResponse("this is the django services page")

def contact(request):

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        c = Contact(name=name, email=email, message=message, date=datetime.today())
        c.save()
        messages.success(request, "Congratulations! Your message has been sent.")


    
    return render(request, "contact.html")
    # return HttpResponse("contact: contact.abdullahkhalid@gmail.com")

def blog(request):
    
    return render(request, "blog.html")


def search(request):
    query = request.GET.get("query")
    results = []
    
    if query:
        results = Contact.objects.filter(name__icontains=query)  # ya email__icontains=query, etc.

    return render(request, "search.html", {"results": results, "query": query})