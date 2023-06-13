from django.contrib import admin
from . import models
admin.site.site_header='Creative learning'


# Register your models here.


class SeoContentModel(admin.ModelAdmin):
    list_display    = ["__str__","Status", ]
    search_fields   = ['index_meta_title','Status']
    list_per_page   = 20

admin.site.register(models.SeoContent, SeoContentModel)

class internetlinkModel(admin.ModelAdmin):
    list_display    = ["__str__","name", "classsubject"]
    search_fields   = ['name','classsubject']
    list_per_page   = 20
    list_filter     = ["name", "classsubject"]

admin.site.register(models.internetlink, internetlinkModel)


class contactModel(admin.ModelAdmin):
    list_display    = ["__str__","name", "email","time"]
    search_fields   = ['name','email']
    list_per_page   = 30
    
admin.site.register(models.contact, contactModel)


class about_usModel(admin.ModelAdmin):
    list_display    = ["__str__","title", "status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["title", "status"]

admin.site.register(models.about_us, about_usModel)


class ownerModel(admin.ModelAdmin):
    list_display    = ["__str__","name", "designation", "status"]
    search_fields   = ['name']
    list_per_page   = 20
    list_filter     = ["designation", "status"]

admin.site.register(models.owner, ownerModel)


class classesModel(admin.ModelAdmin):
    list_display    = ["__str__","name", "status"]
    search_fields   = ['name']
    list_per_page   = 20
    list_filter     = ["name", "status"]

admin.site.register(models.classes, classesModel)


class subjectModel(admin.ModelAdmin):
    list_display    = ["__str__","name", "status"]
    search_fields   = ['name']
    list_per_page   = 20
    list_filter     = ["name", "status"]

admin.site.register(models.subject, subjectModel)


class classsubjectModel(admin.ModelAdmin):
    list_display    = ["name", "classes", "subject"]
    search_fields   = ['classes','subject']
    list_per_page   = 20
    list_filter     = ["classes", "subject"]

admin.site.register(models.classsubject, classsubjectModel)


# class chapterModel(admin.ModelAdmin):
#     list_display    = ["name"]
#     search_fields   = ['name','classsubject']
#     list_per_page   = 20
#     list_filter     = ["name"]

# admin.site.register(models.chapter, chapterModel)



# class subjectchapterModel(admin.ModelAdmin):
#     list_display    = ["name", "classsubject", "chapter"]
#     search_fields   = ['name','classsubject']
#     list_per_page   = 20
#     list_filter     = ["name", "classsubject","chapter"]

# admin.site.register(models.subjectchapter, subjectchapterModel)


class questionModel(admin.ModelAdmin):
    list_display    = ["title", "ques_type", "classsubject","status"]
    search_fields   = ['title']
    list_per_page   = 50
    list_filter     = ["ques_type", "classsubject","status"]

admin.site.register(models.question, questionModel)


class user_regModel(admin.ModelAdmin):
    list_display    = ["name", "reg_date","status"]
    search_fields   = ['name','classes']
    list_per_page   = 50
    list_filter     = ["classes","status"]

admin.site.register(models.user_reg, user_regModel)

class user_answerModel(admin.ModelAdmin):
    list_display    = ["user_reg","question","time","is_correct_ans","status"]
    search_fields   = []
    list_per_page   = 50
    list_filter     = ["status"]

admin.site.register(models.user_answer, user_answerModel)

class user_hit_countModel(admin.ModelAdmin):
    list_display    = ["user_reg","question","hit_count","star"]
    search_fields   = ["question"]
    list_per_page   = 50
    list_filter     = ["star"]

admin.site.register(models.user_hit_count, user_hit_countModel)

class inspire_regModel(admin.ModelAdmin):
    list_display    = ["heading","status"]
    search_fields   = ['heading']
    list_per_page   = 20
    list_filter     = ["status"]

admin.site.register(models.inspire_reg, inspire_regModel)


class upcomingModel(admin.ModelAdmin):
    list_display    = ["heading","status"]
    search_fields   = ['heading']
    list_per_page   = 20
    list_filter     = ["status"]

admin.site.register(models.upcoming, upcomingModel)

