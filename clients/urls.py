from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.client_list, name="client_list"),
    path('new/', views.client_new, name="client_new"),
    path('update/<int:pk>/', views.client_update, name="client_update"),
    path('delete/<int:pk>', views.client_delete, name="client_delete"),
]