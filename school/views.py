from django.shortcuts import render
from django.http import JsonResponse

def students(request):
    if request.method == 'GET':
        student = {'id': 0, 'name': 'John'}
        return JsonResponse(student)