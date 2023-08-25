from django.shortcuts import render, redirect
from . import forms
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'dsshop/about.html')

def about_view(request):
    return render(request,'about.html')

def blog_view(request):
    return render(request,'blog.html')

def contact_view(request):
    return render(request,'contact.html')

def elements_view(request):
    return render(request,'elements.html')

def index_view(request):
    return render(request,'index.html')

def main_view(request):
    return render(request,'main.html')

def performer_view(request):
    return render(request,'performer.html')

def Program_view(request):
    return render(request,'Program.html')

def single_blog_view(request):
    return render(request,'single-blog.html')

def venue_view(request):
    return render(request,'venue.html')

def index2_view(request):
    return render(request,'index2.html')


def register(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm()
    context = {'form': form}

    return render(request, 'registration/register.html', context)