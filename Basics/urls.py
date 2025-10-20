from django.urls import path
from Basics import views

urlpatterns = [
    path('Add/',views.Add,name="Add"),
    path('Calc/',views.Cal,name='nill'),
   
]
