from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
     return self.name
     
    class Meta:
     verbose_name_plural ="categories"

class Movie(models.Model):
    MOVIE = 1
    SERIES = 2
    TRAILERS = 3

    SPECIFICATION_CHOICES =(
     (MOVIE, "Movie"),
      (SERIES, "series"),
      (TRAILERS, "trailers"),

     )

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images',null=True,blank=True)
    description = models.TextField()
    source = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    specification = models.IntegerField(choices=SPECIFICATION_CHOICES,default=MOVIE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
     return self.title
   

class User(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)
   age = models.IntegerField()
   profile_Image = models.ImageField(upload_to='images')
   email = models.EmailField()

   def __str__(self):
    return f"{self.first_name} {self.last_name}"

class settings(models.Model):
  cover_vedio_url = models.TextField()
  cover_title = models.CharField(max_length=200)
  cover_description = models.TextField()

  def __str__(self):
    return f"{self.cover_vedio_url}{self.cover_title}"

       
    
   
    