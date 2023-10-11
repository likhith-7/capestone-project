from django.urls import path, include

from product import views
from .views import getLatestProductsFiltered

urlpatterns = [
    #path('latest-products/', views.LatestProductsList.as_view()),
    path('latest-products/', getLatestProductsFiltered, name='latest'),

]