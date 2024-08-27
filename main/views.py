from django.shortcuts import render, redirect
from .models import *
from rest_framework.views import APIView
from rest_frameork.response import Response
from rest_framework import generaics
from .serialzers import TeacherSerializer


# Create your views here.

class TeacherList(generaics.ListCreateAPIView):
    pass