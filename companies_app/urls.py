from django.urls import path
from .views import StaffListView

urlpatterns = [
    path('emps', StaffListView.as_view(),name='staff-list'),
]