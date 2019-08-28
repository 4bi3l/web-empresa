from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    # el <int:category_id> se traduce en el id o el pk esto es dinamico y se le pasara a la vista 
    path('category/<int:category_id>/', views.category, name="category"),
    
]