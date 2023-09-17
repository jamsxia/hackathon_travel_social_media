from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('user/<str:username>', views.UserVisitedPlacesView.as_view(), name='user-home'),
    path('about/', views.about, name='blog-about'),
]
