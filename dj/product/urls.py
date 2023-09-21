from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.searchProduct),  # 分类增删改查
    path('save/', views.saveTable),
]
