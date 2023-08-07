from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('create', views.create, name='create'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('update/<int:task_id>/', views.update, name='update'),
]
