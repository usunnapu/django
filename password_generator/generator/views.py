import random
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse('this is a another sample test page')

def home(request):
    return render(request, 'generator/home.html', {'password':'passing_value_to_template_from_views'})

def pwgen(request):
    return render(request, 'generator/passwordgenerator.html')

def password(request):

    thepassword = ''
    basechar = list('abcdefghijklmnopqrstuvwxyz')
    upperchar = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    specialchar = list('!@#$%^&*()')
    passwordlength = int(request.GET.get('length'))
    uppercase = request.GET.get('uppercase')
    special = request.GET.get('special')
    num = request.GET.get('numbers')
    
    if uppercase:
        basechar.extend(upperchar)
    if num:
        basechar.extend(numbers)
    if special:
        basechar.extend(specialchar)
    
    for i in range(passwordlength):
        thepassword += random.choice(basechar)

    return render(request, 'generator/password.html', {'password':thepassword})
