from django.urls import path
from .views import MainView, CategoryFilterView

urlpatterns = [
   path("", MainView.as_view(), name='index'),
   path("category/<int:id>", CategoryFilterView.as_view(), name="categoryfilter")
   
]