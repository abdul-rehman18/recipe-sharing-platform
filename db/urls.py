from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login, name='login'),
    path('', views.signup, name='signup'),
    path('category/',views.create_catgeory,name='category'),
    path('recipe/', views.create_recipe, name='recipe_de'),
]