from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from blogapp import models
register = template.Library()

@register.filter(name='aboutus')
def about_us(request):
    about  = models.about_us.objects.filter(status = True).order_by("-id")
    return about

@register.filter(name='ownerreg')
def owner(request):
    owner  = models.owner.objects.filter(status = True).order_by("-id")
    return owner

@register.filter(name='classesreg')
def classes(request):
    classes  = models.classes.objects.filter(status = True).order_by("id")
    return classes

@register.filter(name='user_reg')
def users(request,id):
    users  = models.user_reg.objects.filter(id = id, status = True).order_by("-id")
    return users

@register.filter(name='questionCount')
def ques(request,name):
    question           = models.question.objects.filter(classsubject_id__classes_id__name = name,status=True).count()   
    return question

@register.filter(name='TopicCount')
def topic(request,name):
    topics           = models.classsubject.objects.filter(classes_id__name = name,status=True).count()   
    return topics



@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
