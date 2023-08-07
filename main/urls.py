from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('create', views.create),
    path('delete', views.delete),
    path('find', views.find),
    path('update/<int:task_id>/', views.update, name='update'),

]
