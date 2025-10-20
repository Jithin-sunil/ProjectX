from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('',views.index,name="index"),
    path('Login/',views.Login,name="Login"),
    path('Userreg/',views.Userreg,name="Userreg"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
    path('policereg/',views.policereg,name="policereg"),
    path('advocatereg/',views.advocatereg,name="advocatereg"),
]