from .models import Category, Social, 

def ContextBase(request):
     categories = Category.objects.all()
     social= Social.objects.all() 
    context = {
        'categories' : categories,
        "social" : social,
        }
return context