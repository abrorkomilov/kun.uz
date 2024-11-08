from django.db import models

types = (
     ("ads", "Reklama"),
     ("new", "Yangilik")
)
position_types = (
     ("bosh muhbir", "bosh muhbir"),
     ("miharrir", "miharrir"),
     ("maxsus muhbir", "maxsus muhbir"),
     ("expert", "expert")
)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Tag(models.Model):
     name = models.CharField(max_length=50)

     def __str__(self) -> str:
          return self.name

class New(models.Model):
     type = models.CharField(choices=types, max_length=20)
     create_at = models.DateTimeField(auto_now_add=True)
     title = models.CharField(max_length=256)
     body = models.TextField(max_length=256)
     image = models.ImageField(upload_to="news/", null=True, blank=True)
     category = models.ForeignKey(Category, on_delete=models.SET_NULL, 
                                  null=True, blank=True, related_name="category_news")
     tags = models.ManyToManyField(Tag, blank=True, related_name="tag_news")
     view_count = models.IntegerField(default=0)

     def __str__(self) -> str:
          return f"{self.title}  {self.type}"

class Social(models.Model):
     name = models.CharField(max_length=256)
     link = models.URLField()
     icon = models.ImageField(upload_to="social/")

     def __str__(self) -> str:
          return self.name

class AboutUS(models.Model):
     title = models.CharField(max_length=256)
     body = models.TextField()
     image = models.ImageField(upload_to="about/")
     
     def __str__(self) -> str:
          return self.title
     
class Comments(models.Model):
     name = models.CharField(max_length=256)
     tel_number = models.CharField(max_length=256)
     theme = models.CharField(max_length=256)
     text = models.TextField()

     def __str__(self) -> str:
          return self.name

class Team(models.Model):
     name = models.CharField(max_length=256)
     position = models.CharField(choices=position_types, max_length=50)
     image = models.ImageField(upload_to="team/")

     def __str__(self) -> str:
          return self.name
          