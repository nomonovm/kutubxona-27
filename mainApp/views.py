from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            kurs=request.POST.get('kurs'),
            guruh=request.POST.get('guruh'),
            yosh=request.POST.get('yosh'),
            kitob_soni=request.POST.get('kitob_soni')
        )
        return redirect('talabalar')

    talabalar = Talaba.objects.all()

    search = request.GET.get('search')
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)

    kurs = request.GET.get('kurs')
    if kurs is not None:
        if kurs != 'all':
            talabalar = talabalar.filter(kurs=kurs)

    guruh = request.GET.get('guruh')
    if guruh is not None:
        if guruh != 'all':
            talabalar = talabalar.filter(guruh=guruh)

    guruhlar = Talaba.objects.order_by('guruh').values_list('guruh', flat=True).distinct()
    kurslar = [1, 2, 3, 4]

    context = {
        'talabalar': talabalar,
        'search': search,
        'guruhlar': guruhlar,
        'kurs_query': kurs,
        'guruh_query': guruh,
        'kurslar': kurslar,
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
    kutubxonachilar = Kutubxonachi.objects.all()
    if request.method == "POST":
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get('talaba_id')),
            kitob=Kitob.objects.get(id=request.POST.get('kitob_id')),
            qaytarilgan_sana=request.POST.get('qaytarilgan_sana'),
            kutubxonachi=kutubxonachilar.get(id=request.POST.get('kutubxonachi_id')),
        )
        return redirect('recordlar')

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
        'talabalar': talabalar,
        'kitoblar': kitoblar,
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


def kitob_qoshish_view(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            annotatsiya=request.POST.get('annotatsiya'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id'))
        )
        return redirect('kitoblar')

    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'kitob_qoshish.html', context)

def kutubxonachilar_view(request):
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        'kutubxonachilar': kutubxonachilar,
    }
    return render(request, 'kutubxonachilar.html', context)

def kutubxonachi_details_view(request, kutubxonachi_id):
    kutubxonachi = Kutubxonachi.objects.get(id=kutubxonachi_id)
    context = {
        'kutubxonachi': kutubxonachi,
    }
    return render(request, 'kutubxonachi_details.html', context)