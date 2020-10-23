from django.urls import path     
from . import views

urlpatterns = [
    path('', views.redirect_shows),
    path('shows', views.displayAllShows),
    path('shows/new', views.displayNewShow),
    path('shows/create', views.addShow),	
    path('shows/<int:show_id>', views.displayShow), 
    path('shows/<int:show_id>/edit', views.displayEditShow),
    path('shows/<int:show_id>/update', views.editShow),
    path('shows/<int:show_id>/destroy', views.deleteShow)  
]