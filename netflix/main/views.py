from django.shortcuts import render
from . models import *
from . forms import *

# Create your views here.
def home(request):
    return render(request,"netflix_home.html")
def login(request):
    return render(request,"netflix_login.html")
def movies_home(request):
    background_playing = {
        'source': '<iframe width="560" height="315" src="https://www.youtube.com/embed/pkutd-vmC7I?controls=0&autoplay=1&mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',
        'title': 'Framed For Pleasure - Mkurugenzi Minisodes 3 Ep 1',
        'description':'In this Episode of Minisodes, Mkurugenzi Abel Mutua tells the story of a guy who might end up in jail after being framed for rape by a one night stand. will get you finishing your popcorns'
    }

    all_categories = Category.objects.all()

    context = {
        "background": background_playing,  
        "all_categories":all_categories  
    }
    
    return render(request, "movies_home.html", context)

def add_movie(request):
    print(f"REQUEST METHOD = {request.method}")
    form = MovieForm()

    message = ""
    form_valid = False

    if request.method == 'POST':
        form = MovieForm(request.POST)
        # print(f"FORM: {form}")

        if form.is_valid:
            form.save()
            form_valid = True
            message = "movie created"
  

    context = {
        "movie_form": form,
        "message":message,
        "form_valid":form_valid
    }
    
    return render(request, "create_movie.html", context)