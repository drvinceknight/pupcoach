from django.urls import path
from behaviours import views

urlpatterns = [
    path('behaviours/', views.behaviour_list),
    path('behaviours/<int:pk>/', views.behaviour_detail),
]
