from django.shortcuts import render, redirect
from .models import Companya_foalyati,Companya_tarixi,Murtojat,Img



def index(request):
    companies = Companya_foalyati.objects.all()
    companiya=Companya_tarixi.objects.get(id=1)
    img=Img.objects.all()

    return render(request, 'index.html',context={'companies': companies,'compayas': companiya,'img': img,})

def murojat(request):
    murojat = Murtojat.objects.all()
    return render(request, 'murojat.html',context={'murojat':murojat})

def yuborish(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        kompanyia_name = request.POST['kompanyia_name']
        telefon = request.POST['telefon']
        email = request.POST['email']
        murojat = request.POST['murojat']
        kompaniy_address=request.POST['kompaniy_address']

        Murtojat.objects.create(
            full_name=full_name,
            kompanyia_name=kompanyia_name,
            telefon=telefon,
            email=email,
            murojat=murojat,
            kompaniy_address=kompaniy_address
        )

        return  redirect('index')
    return render(request, 'murojat.html')






