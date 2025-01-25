from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def hello_world(request):
    """
    <h1>Hello World!</h1>

    <p>Django orqali birinchi sahifa!<p>
    """

def home_view(request):
    return render(request, 'index.html')

def talabalar_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar,
    }
    return render(request, 'talabalar.html', context)

def mualliflar_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)

def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_details.html', context)