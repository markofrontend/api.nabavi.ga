from django.urls import path

from . import views

urlpatterns = [
    path('latest-products/', views.LatestProductList.as_view()),
]
