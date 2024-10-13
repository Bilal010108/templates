from django.urls import path
from.views import *

urlpatterns = [
    path('',ProductListView.as_view(), name ='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/', ProductdDeleteView.as_view(), name='product_delete')
]