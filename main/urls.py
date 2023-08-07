from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('aboutus', views.aboutus),
    path('create', views.create),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    # path('find', views.find),
    path('update/<int:task_id>/', views.update, name='update'),

]
