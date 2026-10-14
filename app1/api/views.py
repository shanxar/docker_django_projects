
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class StudentView(APIView):
    def get(self,request):
        try:
            response_data=requests.get("http://app2:8000/api/course/")
            response_data.raise_for_status()
            course_data = response_data.json()

        except requests.RequestException as exc:
            print(f"Course API error: {type(exc).__name__}: {exc}")
            return Response(
                {
                    "error": "Could not reach Course API",
                    "details": str(exc),
                },
                status=status.HTTP_502_BAD_GATEWAY  
                )
        
        return Response({
            "student_id": 1,
            "student_name": "Gowrishankar",
            "course": course_data,
        })