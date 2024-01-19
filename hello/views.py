from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Books

# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello world </h1>")

class BooksView(APIView):
    def get(self,request,format=None):
        books = Books.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = BookSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        
        