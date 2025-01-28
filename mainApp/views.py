from lib2to3.fixes.fix_input import context

from django.shortcuts import render , get_object_or_404, redirect
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

def muallif_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif,
    }
    return render(request, 'muallif_details.html', context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'kitoblar.html', context)

def kitob_details_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob': kitob,
    }
    return render(request, 'kitob_details.html', context)

def recordlar_view(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
    }
    return render(request, 'recordlar.html', context)

def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    talaba.delete()
    return redirect('talabalar')

def talaba_delete_confirm_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba_delete_confirm.html', context)