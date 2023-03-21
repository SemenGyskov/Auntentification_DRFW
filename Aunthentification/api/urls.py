from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('class-add/', ClassCreate.as_view(), name='class-add'),
    path('class/', ClassList.as_view(), name='class_list'),
    path('class/<int:pk>/', ClassAPIUpdate.as_view(), name='class_update'),
    path('student/', StudentList.as_view(), name='student_list'),
    path('student-add/', StudentCreate.as_view(), name='student-add'),
    path('student/<int:pk>/', StudentAPIUpdate.as_view(), name='student_update'),
    path('item/', ItemList.as_view(), name='item_list'),
    path('item-add/', ItemCreate.as_view(), name='Item_add'),
    path('item/<int:pk>/', ItemAPIUpdate.as_view(), name='Item_update'),
    path('auth/', include('rest_framework.urls')),

]