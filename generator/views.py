from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def password(request):

    generated_password = ''

    charactor = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactor.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('speacial'):
        charactor.extend('!@#$%^&*()')

    if request.GET.get('number'):
        charactor.extend('1234567890')

    length = int(request.GET.get('length'),12)+1

    generated_password = ''

    for i in range(1,length):
        generated_password += random.choice(charactor)

    return render(request,'generator/password.html',{'password':generated_password})


def about(request):
    return render(request,'generator/about.html')
