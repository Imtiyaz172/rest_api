from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from .import models
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.db.models import Sum
import datetime
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
import hashlib, socket
import random

# Create your views here.
def index(request):       
        classsubjects      = models.classsubject.objects.filter(status=True).order_by("classes","subject")
        inspire_reg        = models.inspire_reg.objects.filter(status=True).all()
        upcoming           = models.upcoming.objects.filter(status=True).all()
        seo_contain        = models.SeoContent.objects.filter(Status=True).first()
        
        context={
            'classsubjects' : classsubjects,
            'inspire_reg' : inspire_reg,
            'upcoming' : upcoming,
            'seo_contain' : seo_contain,
        }
        return render(request, "blogapp/index.html",context)


# Create your views here.
def about(request):       
    seo_contain        = models.SeoContent.objects.filter(Status=True).first()
    print("xxx")
    context={
            'seo_contain' : seo_contain,
        }    
    return render(request, "blogapp/about.html",context)




def classsubject(request, class_name):
    class_name        = class_name.replace('-', ' ')
    models.classes.objects.filter(name=class_name,status=True).update(view =F('view') + 1)
    subjects   = models.classsubject.objects.filter(classes_id__name=class_name,status=True).order_by("id")    
    seo_contain        = models.classsubject.objects.filter(classes_id__name=class_name,status=True).all()
    
    context={
        'subjects'    : subjects,
        'seo_contain'    : seo_contain,
    }
    return render(request, "blogapp/subject.html",context)


# def subjectquestion(request, class_name, sub_name):
#         classes_name        = class_name.replace('-', ' ')
#         sub_name            = sub_name.replace('-', ' ')
#         subjects            = models.subjectchapter.objects.raw("SELECT cs.id, c.name as class_name, s.name,s.image from blogapp_subjectchapter sc INNER JOIN blogapp_classsubject cs on sc.classsubject_id = cs.id  INNER JOIN blogapp_classes c on cs.classes_id = c.id INNER JOIN blogapp_subject s on cs.subject_id = s.id where sc.status = true and c.name = %s GROUP by s.id ORDER by s.id",[classes_name])
#         # subjects_questions  = models.question.objects.filter(subjectchapter_id__classsubject_id__classes_id__name=classes_name, subjectchapter_id__classsubject_id__subject_id__name=sub_name,status=True).order_by("subjectchapter")
#         subjects_chapter    = models.subjectchapter.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name,status=True).order_by("chapter")
        

#         context={
#             'subjects'    : subjects,
#             'subjects_chapter'    : subjects_chapter,
#     }
#         return render(request, "blogapp/subject.html",context)


def question_list(request, class_name, sub_name):
    classes_name        = class_name.replace('-', ' ')
    sub_name            = sub_name.replace('-', ' ')
    internet            = models.internetlink.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name,status=True).all()
    questions_list      = models.question.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name, status=True).order_by("classsubject")
    # questions_contant   = models.question.objects.filter(subjectchapter_id__classsubject_id__classes_id__name=classes_name, subjectchapter_id__classsubject_id__subject_id__name=sub_name, subjectchapter_id__chapter_id__name=chapter_name,status=True).first() 
    seo_contain = models.question.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name, status=True).all()

    try :
        if request.session['id']:
            questions_contant_u = models.user_answer.objects.filter(question_id__subjectchapter_id__chapter_id__name=chapter_name,user_reg_id = request.session['id']).count()
            
            questions_contant1 = models.user_answer.objects.filter(question_id__subjectchapter_id__chapter_id__name=chapter_name, is_correct_ans='True' ,user_reg_id = request.session['id']).count()
            if questions_contant1 == 0:
                questions_contant1 = 1
            if questions_contant_u == 0:
                questions_contant_u = 1
            percentage = questions_contant1 / questions_contant_u * 100
            
            percentage = int(percentage)
            
            if questions_contant_u>25 and questions_contant_u<50 and percentage < 80:
                questions_contant_e   = models.question.objects.filter(subjectchapter_id__classsubject_id__classes_id__name=classes_name, subjectchapter_id__classsubject_id__subject_id__name=sub_name, subjectchapter_id__chapter_id__name=chapter_name,status=True).first()
                
                context={
                    
                    'questions_contant_e'    : questions_contant_e,
                    'questions_list'    : questions_list,
                    'questions_contant'    : questions_contant,
                }
                return render(request, "blogapp/question_list.html",context)
            
            if questions_contant_u>50 and percentage < 80:
                questions_contant_e   = models.question.objects.filter(subjectchapter_id__classsubject_id__classes_id__name=classes_name, subjectchapter_id__classsubject_id__subject_id__name=sub_name, subjectchapter_id__chapter_id__name=chapter_name,status=True).first()
                questions_contant_video   = models.question.objects.filter(subjectchapter_id__classsubject_id__classes_id__name=classes_name, subjectchapter_id__classsubject_id__subject_id__name=sub_name, subjectchapter_id__chapter_id__name=chapter_name,status=True).first()
                
                context={
                    'questions_contant_e'    : questions_contant_e,
                    'questions_contant_video'    : questions_contant_video,
                    'questions_list'    : questions_list,
                    'questions_contant'    : questions_contant,
                    }
                return render(request, "blogapp/question_list.html",context)
    except:
        pass
    context={

        'questions_list'    : questions_list,
        # 'questions_contant'    : questions_contant,
        'internet'     : internet,
        'seo_contain'     : seo_contain,

        }  
    return render(request, "blogapp/question_list.html",context)  



    return render(request, "blogapp/question_list.html",context)

def question(request, classes_name, sub_name,type_name, id):
    classes_name        = classes_name.replace('-', ' ')
    sub_name            = sub_name.replace('-', ' ')
    type_name           = type_name.replace('-', ' ')
    
    questions           = models.question.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name, ques_level=type_name,id=id ,status=True).first()
    if request.method=="POST":
        direct_input_op   = request.POST.get('direct_input_op')
        taketime        = request.POST.get('taketime')
        if 'direct_input_op' in request.POST:
            cheak_ans     = models.question.objects.filter(id=id ,direct_input_op=direct_input_op)
           
            if request.session.get('id'):
                user_ans = models.user_answer.objects.create(
                    user_reg_id = int(request.session['id']), question_id = questions.id,text_choose = direct_input_op, taketime=taketime,
                )
                
                # cheak_hit = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id)
                # if cheak_hit:
                #     models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(hit_count = F('hit_count')+1)
                # else:
                #     hit_count = models.user_hit_count.objects.create(
                #     user_reg_id = int(request.session['id']), question_id = questions.id ,hit_count = 1
                #     )
                # cheak_star_5  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 1, star = 0)
                # cheak_star_4  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 2, star = 0)
                # cheak_star_3  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 3, star = 0)
                # cheak_star_2  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 4, star = 0)
                # cheak_star_1  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, star = 0)
                if cheak_ans:
                #     if cheak_star_5:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+5)
                #     elif cheak_star_4:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+4)
                #     elif cheak_star_3:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+3)
                #     elif cheak_star_2 :
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+2)
                #     elif cheak_star_1 :
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+1)
                    valid_profiles_id_list      = models.question.objects.values_list('id', flat=True).filter(classsubject_id__classes_id__name = classes_name,classsubject_id__subject_id__name=sub_name,ques_level=type_name,status=True).exclude(id = id)
                    valid_profiles_list = random.sample(list(valid_profiles_id_list), len(valid_profiles_id_list))    
                    models.user_answer.objects.filter(id = user_ans.id).update(is_correct_ans = True, )
                    messages.success(request, "Your ans is right,try this problem")
                    return redirect("/"+"list"+"/"+classes_name.replace(' ', '-')+"/"+sub_name.replace(' ', '-')+"/"+type_name.replace(' ', '-')+"/"+str(valid_profiles_list[0]))
                elif not cheak_ans:
                    messages.warning(request, "Wrong ans try again")
                
            else:
                if cheak_ans:
                    valid_profiles_id_list      = models.question.objects.values_list('id', flat=True).filter(classsubject_id__classes_id__name = classes_name,classsubject_id__subject_id__name=sub_name,ques_level=type_name,status=True).exclude(id = id)
                    valid_profiles_list = random.sample(list(valid_profiles_id_list), len(valid_profiles_id_list))    
                    messages.success(request, "Your ans is right,try this problem")
                    return redirect("/"+"list"+"/"+classes_name.replace(' ', '-')+"/"+sub_name.replace(' ', '-')+"/"+type_name.replace(' ', '-')+"/"+str(valid_profiles_list[0]))
                elif not cheak_ans:
                    messages.warning(request, "Wrong ans try again")
            # if request.session.get('id'):
            #     get_star  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id )    
    
        else:
            ans_op_1        = True if request.POST.get('ans_op_1') else False
            ans_op_2        = True if request.POST.get('ans_op_2') else False
            ans_op_3        = True if request.POST.get('ans_op_3') else False
            ans_op_4        = True if request.POST.get('ans_op_4') else False
            taketime        = request.POST.get('taketime')
            
            

            cheak_ans       = models.question.objects.filter(id=id ,ans_op_1 = ans_op_1,ans_op_2 = ans_op_2,ans_op_3 = ans_op_3,ans_op_4 = ans_op_4)
            if request.session.get('id'):
                user_ans = models.user_answer.objects.create(
                    user_reg_id = int(request.session['id']), question_id =questions.id,ans_choose_op_1 = ans_op_1, ans_choose_op_2 = ans_op_2, ans_choose_op_3 = ans_op_3, ans_choose_op_4 = ans_op_4, taketime=taketime,
                )
                valid_profiles_id_list      = models.question.objects.values_list('id', flat=True).filter(classsubject_id__classes_id__name = classes_name,classsubject_id__subject_id__name=sub_name,ques_level=type_name,status=True).exclude(id = id)
                

                valid_profiles_list = random.sample(list(valid_profiles_id_list), len(valid_profiles_id_list))    
                # cheak_hit = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id)
                # if cheak_hit:
                #     models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(hit_count = F('hit_count')+1)
                # else:
                #     hit_count = models.user_hit_count.objects.create(
                #     user_reg_id = int(request.session['id']), question_id = questions.id ,hit_count = 1
                #     )

                # cheak_star_5  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 1, star = 0)
                # cheak_star_4  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 2, star = 0)
                # cheak_star_3  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 3, star = 0)
                # cheak_star_2  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id, hit_count = 4, star = 0)
                # cheak_star_1  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id,  star = 0)
                if cheak_ans:
                #     if cheak_star_5:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+5)
                #     elif cheak_star_4:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+4)
                #     elif cheak_star_3:
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+3)
                #     elif cheak_star_2 :
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+2)
                #     elif cheak_star_1 :
                #         models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id).update(star = F('star')+1)
                    models.user_answer.objects.filter(id = user_ans.id).update(is_correct_ans = True )
                    messages.success(request, "Your ans is right,try this problem")
                    return redirect("/"+"list"+"/"+classes_name.replace(' ', '-')+"/"+sub_name.replace(' ', '-')+"/"+type_name.replace(' ', '-')+"/"+str(valid_profiles_list[0]))
                   

                elif not cheak_ans:
                    messages.warning(request, "Wrong ans try again")
                # get_star  = models.user_hit_count.objects.filter(user_reg_id = int(request.session['id']), question_id = questions.id )       
            else:   
                if cheak_ans:
                    valid_profiles_id_list      = models.question.objects.values_list('id', flat=True).filter(classsubject_id__classes_id__name = classes_name,classsubject_id__subject_id__name=sub_name,ques_level=type_name,status=True).exclude(id = id)
                    valid_profiles_list = random.sample(list(valid_profiles_id_list), len(valid_profiles_id_list))    
                    messages.success(request, "Your ans is right,try this problem")
                    return redirect("/"+"list"+"/"+classes_name.replace(' ', '-')+"/"+sub_name.replace(' ', '-')+"/"+type_name.replace(' ', '-')+"/"+str(valid_profiles_list[0]))
                elif not cheak_ans:
                    messages.warning(request, "Wrong ans try again")
            
                
    
    else:
        messages.warning(request, "")
    
    seo_contain = models.question.objects.filter(classsubject_id__classes_id__name=classes_name, classsubject_id__subject_id__name=sub_name, ques_level=type_name,id=id ,status=True).first()
    
    context={
        'questions'    : questions,
        'seo_contain'    : seo_contain,
        # 'get_star'    : get_star,
        
        }
    return render(request, "blogapp/question.html",context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')
        models.contact.objects.create(email = email , name = name, massage = massage)
        messages.success(request, "Thankyou for send massage we will give you feedack in your mail")   
    seo_contain        = models.SeoContent.objects.filter(Status=True).first()
    context={
        
        'seo_contain'    : seo_contain,
        
        }
    return render(request,'blogapp/contact.html',context)







from django.core.mail import send_mail
from django.template.loader import render_to_string



def login_attempt(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_md5_obj     = hashlib.md5(password.encode())
        enc_pass    = new_md5_obj.hexdigest()
        user = models.user_reg.objects.filter(email = email,password = enc_pass,status=True).first()
        
        if user is None:
            messages.warning(request, "Wrong Information")
            return render(request,'blogapp/admin/login.html')
        
        otp = str(random.randint(1000 , 9999))
        
        user.otp = otp
        user.save()
        
        request.session['email'] = user.email
        request.session['id'] = user.id
        return redirect('/dashboard/')        
    return render(request,'blogapp/admin/login.html')



def register(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        new_md5_obj     = hashlib.md5(password.encode())
        new_enc_pass    = new_md5_obj.hexdigest() 

        check_user = models.user_reg.objects.filter(email = email).first()
        check_profile = models.Profile.objects.filter(email = email).first()
        
        if check_user or check_profile:
            messages.warning(request, "User already exist")
            return render(request,'blogapp/admin/register.html' )
           
        user = models.user_reg.objects.create(email = email , name = name, password = new_enc_pass)
        otp = str(random.randint(1000 , 9999))
        profile = models.Profile(user = user , email = email , otp = otp) 
        template = render_to_string('blogapp/admin/email.html',{'otp': otp})
        profile.save()
        send_mail(
            'otp',
            template,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        if user:
            request.session['email'] = user.email
            request.session['id'] = user.id

        return redirect('otp')
    return render(request,'blogapp/admin/register.html')

def otp(request):
    email = request.session['email']
    context = {'email':email}
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = models.Profile.objects.filter(email=email).first()
        
        if otp == profile.otp:
            profile = models.user_reg.objects.filter(email = request.session['email']).update(status = True)
            return redirect('/login/')
        else:
            
            messages.warning(request, "Wrong OTP")
            return render(request,'blogapp/admin/otp.html' )
            
        
    return render(request,'blogapp/admin/otp.html' , context)













# def user_reg(request):
#     if request.method=="POST":
#         name            = request.POST['name']
#         email           = request.POST['email']
       
#         password        = request.POST['password']
#         new_md5_obj     = hashlib.md5(password.encode())
#         new_enc_pass    = new_md5_obj.hexdigest()
#         cheak_email     = models.user_reg.objects.filter(email = email)

        
#         if not cheak_email:
#             models.user_reg.objects.create(name = name, email = email,  password = new_enc_pass)
#             messages.success(request, "Your registration has been successfully done Wait 24h for active account")
#             return redirect('/login/')
#         else:
#             messages.warning(request, "There are another account in this gmail")
#             return redirect('/login/')
#     else:
#         messages.warning(request, "")
#     return render(request, "blogapp/admin/register.html")



# def login(request):
#     if request.method=="POST":
#         email     = request.POST['email']
#         password  = request.POST['password']

#         new_md5_obj = hashlib.md5(password.encode())
#         enc_pass    = new_md5_obj.hexdigest()
#         user        = models.user_reg.objects.filter(email = email, password = enc_pass)
#         if user:
#             request.session['email'] = user[0].email
#             request.session['id'] = user[0].id
#             return redirect("/dashboard/")
#         else:
#             messages.warning(request, "Wrong information")
#             return redirect('/login/')
    
#     return render(request, "blogapp/admin/login.html")

def logout(request):
    request.session['email'] = False
    request.session['id'] = False
    return redirect("/")



















# .................................... For Admin..................................................

def dashboard (request):
    if not request.session['id']:
        return redirect('/login/')
    user_profile      = models.user_reg.objects.filter(status = True, id = request.session['id']).first()
    context={
        'user_profile'    : user_profile,
        }
    return render(request, "blogapp/admin/index.html",context)

def history (request):
    if not request.session['id']:
        return redirect('/login/')
    user_history      = models.user_answer.objects.filter(status = True, user_reg_id = request.session['id']).order_by("-id")
    seo_contain = models.user_answer.objects.filter(status = True, user_reg_id = request.session['id']).order_by("-id")
        
    context={
        'user_history'    : user_history,
        'seo_contain'    : seo_contain,
        }
    return render(request, "blogapp/admin/history.html",context)


def subjectresult(request):
    if not request.session['id']:
        return redirect('/login/')
    
    classes    = models.classsubject.objects.filter(status=True).all()
    
    context={
        'classes'    : classes,
        }
    return render(request, "blogapp/admin/classlist.html",context)

def classlistimprove(request):
    if not request.session['id']:
        return redirect('/login/')
    
    classes    = models.classsubject.objects.filter(status=True).all()
    
    context={
        'classes'    : classes,
        }
    return render(request, "blogapp/admin/classlist_improvement.html",context)


def subjectlist(request, class_name):
    class_name        = class_name.replace('-', ' ')
    if not request.session['id']:
        return redirect('/login/')
    
    
    subjectsre   = models.classsubject.objects.filter(classes_id__name=class_name,status=True).order_by("id")
        

    context={
        'subjectsre'    : subjectsre,
    }
    return render(request, "blogapp/admin/subjectlist.html",context)
        
def subjectlistimprovement(request, class_name):
    class_name        = class_name.replace('-', ' ')
    if not request.session['id']:
        return redirect('/login/')
    
    
    subjectsre   = models.classsubject.objects.filter(classes_id__name=class_name,status=True).order_by("id")
        
    context={
        'subjectsre'    : subjectsre,
    }
    return render(request, "blogapp/admin/subjectlist_improvement.html",context)


# def chapter_list_improvement(request, class_name,sub_name):
#     class_name        = class_name.replace('-', ' ')
#     sub_name            = sub_name.replace('-', ' ')
#     if not request.session['id']:
#         return redirect('/login/')
    
#     chapter_list   = models.subjectchapter.objects.filter(classsubject_id__classes_id__name=class_name, classsubject_id__subject_id__name=sub_name,status=True).order_by("id")

    
#     context={
#         'chapter_list'    : chapter_list,
        
#     }
#     return render(request, "blogapp/admin/chapterlist_improvement.html",context)


def improvement(request, class_name,sub_name):
    class_name        = class_name.replace('-', ' ')
    sub_name            = sub_name.replace('-', ' ')
    if not request.session['id']:
        return redirect('/login/')
    
    all_ques_c     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id']).count()
    secound     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,is_correct_ans='True',user_reg_id = request.session['id'])[:50].count()
    all_ans     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,is_correct_ans='True',user_reg_id = request.session['id']).count()
    all_ques50     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id'])[25:50]
    all_ques25     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id'])[0:25]
    all_ques     =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id'])[50:]
    # all_ques = int(all_ques)
    correct_count = 0
    correct_count25 = 0
    correct_count50 = 0
    
    for i in all_ques:
        if i.is_correct_ans: correct_count += 1
        print(i.is_correct_ans,i.id)
    for i in all_ques25:
        if i.is_correct_ans: correct_count25 += 1
        print(i.is_correct_ans,i.id)
    for i in all_ques50:
        if i.is_correct_ans: correct_count50 += 1
        print(i.is_correct_ans,i.id)

    # all_ques = all_ques.filter(is_correct_ans=True)

    # if all_ques < 25:
    #     first_persent = first / all_ques * 100
     
    # if all_ques > 25:
    #     first_persent = first / 25 * 100
    #     print(first_persent)

    # if all_ques < 50:
    #     secound_persent = secound / all_ques * 100
    #     print(secound_persent)
        
    # if all_ques > 50:
    #     all_ans_persent = all_ans / all_ques * 100
    seo_contain = models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id']).count()
    context={
    
    # 'all_ans_persent'    : all_ans_persent,
    'correct_count'    : correct_count,
    'correct_count25'    : correct_count25,
    'correct_count50'    : correct_count50,
    'all_ques_c'    : all_ques_c,
    'seo_contain'    : seo_contain,
    # 'first_persent'    : first_persent,
    # 'secound_persent'    : secound_persent,
    }
    
    
    return render(request, "blogapp/admin/improvement_result.html",context)



def subjectperform(request, class_name,sub_name):
    class_name        = class_name.replace('-', ' ')
    sub_name            = sub_name.replace('-', ' ')
    
    if not request.session['id']:
        return redirect('/login/')
    
    answerd    =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id']).count()
    right      =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name, is_correct_ans='True' ,user_reg_id = request.session['id']).count()
    wrong      =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name, is_correct_ans='False' ,user_reg_id = request.session['id']).count()
    spend      =  models.user_answer.objects.filter(question_id__classsubject_id__subject_id__name=sub_name ,question_id__classsubject_id__classes_id__name=class_name ,user_reg_id = request.session['id']).aggregate(Sum('taketime'))['taketime__sum'],
    spend = float('.'.join(str(ele) for ele in spend))
    context={
        'answerd'    : answerd,
        'right'    : right,
        'wrong'    : wrong,
        'spend'    : spend,
    }
    return render(request, "blogapp/admin/sub_result.html",context)




def edit_profile (request):
    if not request.session['id']:
        return redirect('/login/')
    edit_profile      = models.user_reg.objects.filter(status = True, id = request.session['id']).first()
    context={
        'edit_profile' : edit_profile,
    }
    if request.method=="POST":
        name                = request.POST['name']
        address             = request.POST['address']
        
          
        user_image = ""
        if bool(request.FILES.get('user_image', False)) == True:
            
            file = request.FILES['user_image']
            user_image = "user_image/"+file.name
            if not os.path.exists(settings.MEDIA_ROOT+"user_image/"):
                os.mkdir(settings.MEDIA_ROOT+"user_image/")
            default_storage.save(settings.MEDIA_ROOT+"user_image/"+file.name, ContentFile(file.read()))
        models.user_reg.objects.filter(id = request.session['id']).update(name = name, user_image = user_image, address = address )
        
        messages.success(request, "Update Complete")
        
        return redirect('/dashboard/')
    return render(request, "blogapp/admin/edit_profile.html",context)

