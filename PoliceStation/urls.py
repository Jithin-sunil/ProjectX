from django.urls import path
from PoliceStation import views
app_name="PoliceStation"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('Logout/',views.Logout,name="Logout"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Addcase/',views.Addcase,name="Addcase"),
    path('casedelete/<int:id>',views.casedelete,name="casedelete"),

    path('viewrequest/',views.viewrequest,name="viewrequest"),
    path('verifyrequest/<int:id>/<int:status>',views.verifyrequest,name="verifyrequest"),

]