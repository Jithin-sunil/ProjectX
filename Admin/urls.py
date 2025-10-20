from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
      path('Logout/', views.Logout,name="Logout"),
      path('Homepage/', views.Homepage,name="Homepage"),
      path('Admin/', views.Admin,name="Admin"),
      path('deladmin/<int:did>/',views.deladmin,name="deladmin"),
      path('editadmin/<int:eid>/',views.editadmin,name="editadmin"),
      path('District/',views.District,name="District"),
      path('deldistrict/<int:did>/',views.deldistrict,name="deldistrict"),
      path('type/',views.type,name="type"),
      path('editdistrict/<int:eid>/',views.editdistrict,name="editdistrict"),
      path('place/',views.Place, name="place"),
      path('delplace/<int:pid>/',views.delplace,name="delplace"),
      path('editplace/<int:peid>/',views.editplace,name="editplace"),
      path('viewadvocates/',views.viewadvocates,name="viewadvocates"),
      path('acceptadvocates/<int:aid>/',views.acceptadvocates,name="acceptadvocates"),
      path('rejectadvocates/<int:rid>/',views.rejectadvocates,name="rejectadvocates"),
      path('viewpolicestation/',views.viewpolicestation,name="viewpolicestation"),
      path('acceptstation/<int:aid>/',views.acceptstation,name="acceptstation"),
      path('rejectstation/<int:aid>/',views.rejectstation,name="rejectstation"),
      path('deletetype/<int:id>/',views.deletetype,name="deletetype"),
      path('edittype/<int:id>/',views.edittype,name="edittype"),

      path('viewcomplaints/',views.viewcomplaints,name="viewcomplaints"),
      path('replycomplaint/<int:cid>/',views.replycomplaint,name="replycomplaint"),
]
  

