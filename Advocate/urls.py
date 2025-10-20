from django.urls import path
from Advocate import views
app_name="Advocate"

urlpatterns = [
    path('HomePage/',views.HomePage,name="HomePage"),
    path('Logout/',views.Logout,name="Logout"),
    path('MyProfile/',views.MyProfile,name="MyProfile"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('changepwd/',views.changepwd,name="changepwd"),
    path('ViewBooking/',views.ViewBooking,name="ViewBooking"),
    path('verifybooking/<int:id>/<int:status>/',views.verifybooking,name="verifybooking"),

    path('viewstation/',views.viewstation,name="viewstation"),
    path('viewcase/<int:id>',views.viewcase,name="viewcase"),
    path('sendrequest/<int:id>',views.sendrequest,name="sendrequest"),

    path('myrequest/',views.myrequest,name="myrequest"),
    path('casedetails/<int:id>',views.casedetails,name="casedetails"),
    path('sendbail/<int:id>',views.sendbail,name="sendbail"),




    
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
]