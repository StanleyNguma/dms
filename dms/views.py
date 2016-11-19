from django.http import JsonResponse
from django.shortcuts import render
from django import forms
import datetime


def index(request):
    now = datetime.datetime.now()
    if 'email' in request.session:
        email = request.session['email']
        return render(request, 'index.html', {"username": email, "current_year": now.year})
    else:
        return render(request, 'login.html')


def login(request):
    return render(request, 'login.html')


def auth(request):
    response = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email == password:
            request.session['email'] = email
            response['status'] = '00'
            response['message'] = 'Login successful'
        else:
            response['status'] = '01'
            response['message'] = 'The username/password combination is incorrect'
    else:
        response['status'] = '01'
        response['message'] = 'This is not a post request'
    return JsonResponse(response)


def upload_files(request):
    files = request.FILES
    print str(files)
    for f in files:
        print f
    return JsonResponse({
        'status': '00',
        'message': 'Successfully uploaded the file'
    })
