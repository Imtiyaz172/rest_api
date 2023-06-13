
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('list/<str:class_name>/',views.classsubject, name="class"),
    # path('<str:class_name>/<str:sub_name>',views.subjectquestion),
    path('list/<str:class_name>/<str:sub_name>/',views.question_list, name="subject"),
    path('list/<str:classes_name>/<str:sub_name>/<str:type_name>/<int:id>/',views.question,name="questions"),

    path('contact/',views.contact, name="contact"),
    path('about/',views.about, name = "about"),

    path('login/' , views.login_attempt , name="login"),
    path('user-reg/' , views.register , name="register"),
    path('otp/' , views.otp , name="otp"),
    path('logout/',views.logout),

    
    #........ Admin Urls..........
    path('dashboard/', views.dashboard, name="dashboard"),
    path('user-history/', views.history, name="history"),
    path('sub-list/', views.subjectresult),
    path('sub-result/<str:class_name>/',views.subjectlist),
    path('sub-result/<str:class_name>/<str:sub_name>/',views.subjectperform),
    path('class-list-improvement/', views.classlistimprove),
    path('sub-list-improvement/<str:class_name>/',views.subjectlistimprovement),
    path('improvement/<str:class_name>/<str:sub_name>',views.improvement),
    path('edit-profile/', views.edit_profile),
]
