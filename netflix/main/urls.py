from django.urls import path
from . views import *


urlpatterns = [
    path('',home, name='netflix-home'),
    path('login/',login, name='user-login'),
    path('movies/',movies_home, name="movies"),
    path('add-movie/',add_movie, name="add-movie")
]

