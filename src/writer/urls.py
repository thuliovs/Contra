from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='writer-dashboard'),
    path('my-articles/', views.my_articles, name='my-articles'),
    path('create-article/', views.create_article, name='create-article'),
    path('update-article/<int:id>', views.update_article, name='update-article'),
]