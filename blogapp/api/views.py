from rest_framework import serializers
from blogapp import models
from . import serializers
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class about_usViewSet(viewsets.ModelViewSet):
    queryset = models.about_us.objects.all()
    serializer_class = serializers.about_usSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]



class about_usViewSet(viewsets.ModelViewSet):
    queryset = models.about_us.objects.all()
    serializer_class = serializers.about_usSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

@api_view(['GEt'])
def getclasses(request):
    serializer = serializers.classsubjectSerializer(data=request.data)
    if serializer.is_valid():
        
        response = {
            'code': '200',
            'Classes': serializer.get_classes(request),
            'status': 'success'
        }
        return Response(response)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def getclass_subject(request):
    serializer = serializers.classsubjectSerializer(data=request.data)
    if serializer.is_valid():
        
        response = {
            'code': '200',
            'Subject': serializer.get_class_subject(request),
            'status': 'success'
        }
        return Response(response)
    else:
        return Response(serializer.errors)




@api_view(['POST'])
def getquestion(request):
    serializer = serializers.questionSerializer(data=request.data)
    if serializer.is_valid():
        
        response = {
            'code': '200',
            'Question': serializer.get_question(request),
            'status': 'success'
        }
        return Response(response)
    else:
        return Response(serializer.errors)



