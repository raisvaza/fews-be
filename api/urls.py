from django.urls import path
from . import views

urlpatterns = [
    path('get-item/', views.getItem),
    path('add-item/', views.addItem),
    path('get-pos/', views.get_pos),
    path('get-reading/rainfall', views.get_reading_rainfall),
    path('get-reading/water-level', views.get_reading_waterlevel),


    path('get-latest-predict/', views.get_latest_predict_for_every_pos)
]