from django.shortcuts import render
from django.views import View
from django.shortcuts import get_list_or_404
from .models import Category, New, Social
# Create your views here.

class MainView(View):
    def get(self, request):
        context = {

        }
        return render(request, template_name='index.html', context=context)
        
class CategoryFilterView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        news = New.objects.filter(type="news", category=category).order_by("-create_at") [:20]
        context = {
            "news" : news,
            "category_name" : category.name,
        }
        return render(request, template_name="category_news.html", context=context)
