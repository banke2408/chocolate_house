from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seasonal-flavors/', views.list_seasonal_flavors, name='list_seasonal_flavors'),
    path('add-seasonal-flavor/', views.add_seasonal_flavor, name='add_seasonal_flavor'),
    path('update-seasonal-flavor/<int:flavor_id>/', views.update_seasonal_flavor, name='update_seasonal_flavor'),
    path('delete-seasonal-flavor/<int:flavor_id>/', views.delete_seasonal_flavor, name='delete_seasonal_flavor'),
    path('feedback/', views.list_feedback, name='list_feedback'),
    path('add-feedback/', views.add_feedback, name='add_feedback'),
    path('ingredients/', views.list_ingredients, name='list_ingredients'),
    path('add-ingredient/', views.add_ingredient, name='add_ingredient'),
    path('update-ingredient/<int:ingredient_id>/', views.update_ingredient, name='update_ingredient'),
    path('delete-ingredient/<int:ingredient_id>/', views.delete_ingredient, name='delete_ingredient'),
]

