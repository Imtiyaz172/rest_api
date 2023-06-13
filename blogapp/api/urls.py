from django.db import router
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register("about", views.about_usViewSet, basename='about_us')


urlpatterns = [
    path('', include(router.urls)),
    path('classlist/', views.getclasses, name='api.classes'),
    path('classSubjectList/', views.getclass_subject, name='api.classSubject'),
    path('questionlist/', views.getquestion, name='api.question'),
    
]