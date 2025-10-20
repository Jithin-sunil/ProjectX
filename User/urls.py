from django.urls import path
from User import views
app_name="User"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('Logout/',views.Logout,name="Logout"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('viewadvocates/',views.viewadvocates,name="viewadvocates"),
    path('booking/<int:lawid>/',views.booking,name="booking"),
    path('viewbooking/',views.viewbooking,name="viewbooking"),
    path('uploaddocs/<int:bid>/',views.uploaddocs,name="uploaddocs"),



    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),

    path('complaint/',views.complaint,name="complaint"),
    path('delete_complaint/<int:cid>/',views.delete_complaint,name="delete_complaint"),
]