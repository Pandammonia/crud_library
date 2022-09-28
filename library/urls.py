from django.contrib import admin
from django.urls import path, include
from . import views

app_name='library'
urlpatterns = [
    path('', views.index, name='index'),
    path('addbook/', views.addbook, name='addbook'),
    path('addauthor/', views.addauthor, name='addauthor'),
    path('sort/', views.sort, name='sort'),
    path('search/', views.search, name='search'),
    path('search/searchresults/', views.searchresults, name='search_results'),
    path('<slug:slug>/', views.bookdetails, name='detail'),
    path('<slug:slug>/delete/', views.bookdelete, name='delete'),
    path('<slug:slug>/update/', views.bookupdate, name='update'),
    path('author/<slug:slug>/', views.authordetail, name='authordetail'),
]