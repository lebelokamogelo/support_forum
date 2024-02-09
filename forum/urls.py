from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('topics/', views.my_topics, name='topics'),
    path('topic/<str:uuid>/', views.detail_topic, name='detail-topic'),
]
