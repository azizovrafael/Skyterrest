from django.shortcuts import render ,get_object_or_404,HttpResponseRedirect,HttpResponse
from .forms import *
from .models import *
from django.db.models import Q

def Skyterest_Home(request):
    app = Seher_Adlari.objects.all()
    #querry = request.GET.get('q')
    #if querry:
    #    app = app.filter(id__icontains=querry)
    return render(request,'index.html',{'app':app})

def Skyterest_Services_View(request):
    app = Service_Adlari_2.objects.all()
    querry = request.GET.get('City_Name')
    if querry:
        print(querry)
        app = app.filter(seherler__icontains=querry)
    return render(request,'Services.html',{'app':app})

def Skyterest_Service_Tpye(request):
    app = Service_Adlari_3.objects.all()
    query = request.GET.get('Service_Type')
    if query:
       app = app.filter(
          Q(servis_seher__icontains=query)
       ).distinct()
       #app = app.filter(servis_seher__icontains=query)
    return render(request,'Type.html',{'app':app})

def Skyterest_Service_Tpye_Detail(request):
    app = Service_Adlari_3.objects.all()
    query = request.GET.get('Service_Type_Detail')
    if query:
       app = app.filter(
          Q(servis_mekan__icontains=query)
       ).distinct()
       #app = app.filter(servis_seher__icontains=query)
    return render(request,'Detail.html',{'app':app})
