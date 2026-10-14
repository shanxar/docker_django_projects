from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class CourseView(APIView):
    def get(self, request):
        return Response({
            "course_id": 101,
            "course_name": "Docker with Django REST Framework",
            "duration": "2 weeks",
            "status": "available",
        })