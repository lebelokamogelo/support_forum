from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('create-account/', views.create_account, name='create-account'),
]
