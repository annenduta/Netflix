from django.urls import path, include #importing path and include
from . views import *
from main.views import add_movie

urlpatterns = [
    path('home/', home, name='staff-home'),
    path('movielist/',movielist,name="movielist"),
    path("moviedetails/<movie_id>",moviedetails,name="moviedetails"),
    # The <movie_id > after the / takes in the value sent into the path directed to the views and becomes the argument for the view.
    path("adminaddmovie/",add_movie,name="admin_add_movie"),
    path('categorylist/',categorylist,name="categorylist"),
    path('userlist',userlist,name="userlist"),
    path('settings',adminsettings,name="adminsettings"),   
]
