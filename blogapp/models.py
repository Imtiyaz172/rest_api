from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os
from django.urls import reverse

# Create your models here.


class about_us(models.Model):
    title       = models.CharField(max_length=50)
    title_url       = models.CharField(max_length=200,blank= True)
    logo        = models.ImageField(upload_to="logo/",blank= True)
    phone       = models.CharField(max_length=16,blank=True)
    email       = models.CharField(max_length=36,blank=True)
    address     = models.CharField(max_length=76,blank=True)
    facebook    = models.CharField(max_length=276,blank=True)
    twiter      = models.CharField(max_length=76,blank=True)
    location    = models.TextField(blank=True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status      = models.BooleanField(default = True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'about_us'
        verbose_name_plural = 'about_us' 


class owner(models.Model):
    name        = models.CharField(max_length=100)
    title_url       = models.CharField(max_length=200,blank= True)
    designation = models.CharField(max_length=76,blank=True)
    image       = models.ImageField(upload_to="owner/",blank= True)
    phone       = models.CharField(max_length=16,blank=True)
    email       = models.CharField(max_length=36,blank=True)
    facebook    = models.CharField(max_length=276,blank=True)
    instagram   = models.CharField(max_length=276,blank=True)
    twiter      = models.CharField(max_length=76,blank=True)
    speach      = models.TextField(blank=True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status      = models.BooleanField(default = True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'owner'
        verbose_name_plural = 'owner' 


class classes(models.Model):
    name          = models.CharField(max_length=100)
    image         = models.FileField(upload_to="class/",blank= True)
    view          = models.IntegerField(default=0)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    update            = models.DateField(auto_now_add=True, blank= True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("class", kwargs={"class_name": self.name})

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'  

class subject(models.Model):
    name          = models.CharField(max_length=100)
    image         = models.FileField(upload_to="subject/",blank= True)
    view          = models.IntegerField(default=0)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.name     
    class Meta:
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'  


class classsubject(models.Model):
    name          = models.CharField(max_length=100,blank= True)
    subject       = models.ForeignKey(subject, on_delete=models.CASCADE)
    classes       = models.ForeignKey(classes, on_delete=models.CASCADE)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)
    view          = models.IntegerField(default=0)
    def __str__(self):
        return self.name   
    def get_absolute_url(self):
        return reverse("subject", kwargs={
            "class_name": self.classes.name,
            "sub_name" : self.subject.name,
        })  
    class Meta:
        verbose_name = 'Topic of language'
        verbose_name_plural = 'Topics of language' 



class internetlink(models.Model):
    name          = models.CharField(max_length=200,blank= True)
    classsubject  = models.ForeignKey(classsubject, on_delete=models.CASCADE)
    link          = RichTextUploadingField(blank=True)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.name     
    class Meta:
        verbose_name = 'internet link'
        verbose_name_plural = 'internet links' 




class contact(models.Model):
    name          = models.CharField(max_length=100,blank= True)
    email          = models.CharField(max_length=100,blank= True)
    massage          = models.TextField(blank= True)
    time          = models.DateTimeField(auto_now_add = True)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.name     
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contact' 




# class subjectchapter(models.Model):
#     name          = models.CharField(max_length=200,blank= True)
#     chapter       = models.ForeignKey(chapter, on_delete=models.CASCADE)
#     classsubject  = models.ForeignKey(classsubject, on_delete=models.CASCADE)
#     # learning_content  = RichTextUploadingField(blank=True)
#     Chapter_pdf   = models.FileField(upload_to="pdf/",blank= True)
#     Chapter_video_1 = models.TextField(blank=True)
#     Chapter_video_2 = models.TextField(blank=True)
#     Chapter_video_3 = models.TextField(blank=True)
#     Chapter_video_4 = models.TextField(blank=True)
#     Chapter_video_5 = models.TextField(blank=True)
#     Chapter_video_6 = models.TextField(blank=True)
#     Chapter_pdf_internet   = models.FileField(upload_to="pdf/",blank= True)
#     status        = models.BooleanField(default = True)

#     def __str__(self):
#         return self.name     
#     class Meta:
#         verbose_name = 'chapter of subject'
#         verbose_name_plural = 'chapters of subjects' 



class question(models.Model):
    classsubject  = models.ForeignKey(classsubject, on_delete=models.CASCADE)
    ques_type = (
        ('MCQ', 'MCQ'),
        ('Multiple_MCQ', 'Multiple_MCQ'),
        ('text', 'text'),
        ('image', 'image'),
        ('Multiple_image', 'Multiple_image'),
    )
    ques_type       = models.CharField(max_length=20, choices=ques_type)
    ques_level = (
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),    
        ('Easy', 'Easy'),
    )
    ques_level      = models.CharField(max_length=20, choices=ques_level)
    title           = models.CharField(max_length=200,blank= True)
    title_url       = models.CharField(max_length=200,blank= True)
    body            = RichTextField(blank=True)
    image           = models.FileField(upload_to="question/",blank= True)
    direct_input_op = models.CharField(max_length=200,blank= True)
    text_op_1       = models.CharField(max_length=50,blank= True)
    text_op_2       = models.CharField(max_length=50,blank= True)
    text_op_3       = models.CharField(max_length=50,blank= True)
    text_op_4       = models.CharField(max_length=50,blank= True)
    img_op_1        = models.FileField(upload_to="question/",blank= True)
    img_op_2        = models.FileField(upload_to="question/",blank= True)
    img_op_3        = models.FileField(upload_to="question/",blank= True)
    img_op_4        = models.FileField(upload_to="question/",blank= True)
    ans_op_1        = models.BooleanField(default = False)
    ans_op_2        = models.BooleanField(default = False)
    ans_op_3        = models.BooleanField(default = False)
    ans_op_4        = models.BooleanField(default = False)
    hint            = RichTextField(blank=True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    view          = models.IntegerField(default=0)
    lastmod            = models.DateField(auto_now_add=True, blank= True)
    status          = models.BooleanField(default = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("questions", kwargs={
            "classes_name" : self.classsubject.classes.name,
            "sub_name" : self.classsubject.subject.name,
            "type_name" : self.ques_level,
            "id": str(self.id),
            })  

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions' 



class user_reg(models.Model):
    name               = models.CharField(max_length=100,blank=True)
    otp                = models.CharField(max_length=6, blank=True)
    email              = models.EmailField(max_length=80, blank=True)
    user_image         = models.ImageField(upload_to = "user_image/", blank = True)
    password           = models.CharField(max_length=100)
    address            = models.TextField(blank=True) 
    classes            = models.ForeignKey(classes, on_delete=models.CASCADE,blank = True, null =True)
    point              = models.IntegerField(default=0)
    reg_date           = models.DateField(auto_now_add=True)
    status            = models.BooleanField(default=False)
    def __str__(self):
        return self.name     
    class Meta:
        verbose_name = 'User information'
        verbose_name_plural = 'Users informations' 


class Profile(models.Model):
    user = models.ForeignKey(user_reg ,on_delete=models.CASCADE)
    email = models.CharField(max_length=90,blank=True)
    otp = models.CharField(max_length=6)
    


class user_answer(models.Model):
    user_reg      = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    question      = models.ForeignKey(question, on_delete=models.CASCADE)
    text_choose   = models.CharField(max_length=50,blank= True)
    ans_choose_op_1      = models.BooleanField(default = False)
    ans_choose_op_2      = models.BooleanField(default = False)
    ans_choose_op_3      = models.BooleanField(default = False)
    ans_choose_op_4      = models.BooleanField(default = False)
    is_correct_ans  = models.BooleanField(default = False)
    time          = models.DateTimeField(auto_now_add = True)
    taketime   = models.CharField(max_length=50,blank= True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return str(self.user_reg)     
    class Meta:
        verbose_name = 'user_answer'
        verbose_name_plural = 'user_answers' 


class user_hit_count(models.Model):
    user_reg      = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    question      = models.ForeignKey(question, on_delete=models.CASCADE)
    hit_count      = models.IntegerField(default=0)
    star          = models.IntegerField(default=0)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return str(self.user_reg)     
    class Meta:
        verbose_name = 'user_hit_count'
        verbose_name_plural = 'user_hit_counts' 


class inspire_reg(models.Model):
    heading       = models.CharField(max_length=200,blank= True)
    body          = models.TextField(blank= True)
    slider_image  = models.ImageField(upload_to = "inspire_reg/", blank = True)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.heading     
    class Meta:
        verbose_name = 'inspire of registration'
        verbose_name_plural = 'inspire of registration' 

class upcoming(models.Model):
    heading       = models.CharField(max_length=200,blank= True)
    date          = models.TextField(blank= True)
    image        = models.ImageField(upload_to = "upcoming/", blank = True)
    title_url       = models.CharField(max_length=200,blank= True)
    seo_title     = models.TextField(blank=True)
    seo_discription     = models.TextField(blank=True)
    seo_keyword     = models.TextField(blank=True)
    status        = models.BooleanField(default = True)

    def __str__(self):
        return self.heading     
    class Meta:
        verbose_name = 'upcoming'
        verbose_name_plural = 'upcoming' 


class SeoContent(models.Model):
    index_meta_title            = models.TextField(blank=True)
    index_meta_description      = models.TextField(blank=True)
    index_meta_keywords         = models.TextField(blank=True)
    inspire_reg_title           = models.TextField(blank=True)
    inspire_reg_description     = models.TextField(blank=True)
    inspire_reg_keywords        = models.TextField(blank=True)
    upcoming_title               = models.TextField(blank=True)
    upcoming_description         = models.TextField(blank=True)
    upcoming_keywords            = models.TextField(blank=True)
    contact_title            = models.TextField(blank=True)
    contact_description      = models.TextField(blank=True)
    contact_keywords         = models.TextField(blank=True)
    about_us_title              = models.TextField(blank=True)
    about_us_description        = models.TextField(blank=True)
    about_us_keywords           = models.TextField(blank=True)
    Status        = models.BooleanField(default = True)

    def __str__(self):
        return self.index_meta_title 
    class Meta:
        verbose_name = 'Seo Content'
        verbose_name_plural = 'Seo Contents'