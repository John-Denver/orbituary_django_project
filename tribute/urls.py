from django.urls import path
from . import views

urlpatterns = [
    path('submit_obituary/', views.submit_obituary, name='submit_obituary'),
    path('view_obituaries/', views.view_obituaries, name='view_obituaries'),

]
