from django.shortcuts import render
from main.models import *
from main.forms import *
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    movies = Movie.objects.all()
    categories = Category.objects.all()
    users = User.objects.all()

    context = {
        "movies":movies,
        "categories":categories,
        "users":users
    }
    return render(request,"home.html",context)
def movielist(request):
    movies=Movie.objects.all()
    context={
        "movies":movies,
    }
    return render(request,"movielist.html",context)
def moviedetails(request,movie_id):
    # The parameteR movie_id recieves the argument via the sent url
    # The id passed as the functions parameter will be the movie selected id so it can be used to get the details.
    selected_movie=Movie.objects.filter(id=movie_id).first()
    # the var selected_movie now holds the fmovie being searched for after being filtered via the recieved id
    context = {
        "selected_movie":selected_movie
    }
    return render(request,"moviedetails.html",context)# this line of code then sends the functions answer to the template
def categorylist(request):
    categories=Category.objects.all()
    context={
        "category":categories
    }
    return render(request,"categorylist.html",context)
def adminsettings(request):
    return render(request,"settings.html",)
def userlist(request):
    return render(request,"userlist.html")
