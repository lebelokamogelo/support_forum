from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('create-account/', views.create_account, name='create-account'),
]
