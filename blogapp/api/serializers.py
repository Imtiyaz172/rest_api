from django.db.models import fields
from blogapp import models
from rest_framework import serializers


class about_usSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.about_us
        fields = ['id','title','logo']


class pythonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.classes
        fields = ['id','name']

class classsubjectSerializer(serializers.ModelSerializer):
    def get_classes(self, request, **kwargs):
        classs_list = models.classes.objects.all()
        classes = []
        for i in classs_list:
            data = {
                'id': i.id,
                'name': i.name,
                'image': str(i.image),
            }
            classes.append(data)
      
        return classes
    def get_class_subject(self, request, **kwargs):
        class_id = request.data["class_id"]
        subject_list = models.classsubject.objects.filter(classes_id = class_id)


        class_subject_list = []
        for i in subject_list:
            data = {
                'id': i.id,
                'name': i.name,
                'subject_name': i.subject.name,
                'classes': i.classes.name,
            }
            class_subject_list.append(data)
        return class_subject_list

    class Meta:
        model = models.classsubject
        fields = []
        extra_kwargs = {
            'subject': {'validators': []},
            'classes': {'validators': []},
        }
class questionSerializer(serializers.ModelSerializer):
    def get_question(self, request, **kwargs):
        
        classsubject_id = request.data["classsubject_id"]
        question = models.question.objects.filter(classsubject_id = classsubject_id)


        question_list = []
        for i in question:
            data = {
                'id': i.id,
                'name': i.title,
                'subject_name': i.classsubject.subject.name,
                'ques_type': i.ques_type,
                'ques_level': i.ques_level,
                'text_op_1': i.text_op_1,
                'text_op_2': i.text_op_2,
                'text_op_3': i.text_op_3,
                'text_op_4': i.text_op_4,
                'view': i.view,
                'ans_op_1': i.ans_op_1,
                'ans_op_2': i.ans_op_2,
                'ans_op_3': i.ans_op_3,
                'ans_op_4': i.ans_op_4,
            }
            question_list.append(data)
        return question_list

    class Meta:
        model = models.question
        fields = []
        extra_kwargs = {
            'classsubject': {'validators': []},
        }