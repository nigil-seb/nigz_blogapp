from django.contrib import admin
from django.urls import path, include

from blogapp import views

urlpatterns = [
    path('',views.blogview,name='blogview'),
    path('delete/<int:blogid>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('cbvblog/',views.BlogListView.as_view(),name='cbvblog'),
    path('cbvdetail/<int:pk>/',views.BlogDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.BlogUpdateView.as_view(), name='cbvupdate')
]
