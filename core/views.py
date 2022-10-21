from django.shortcuts import render, HttpResponse

# Create your views here.
def home (request):
    
    return  render (request,'tcore/home.html')

def about (request):
    return render (request,'tcore/about.html')



def contact (request):
    return  render (request,'tcore/contact.html')