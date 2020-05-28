from django.shortcuts import render ,redirect
from .models import Apps,Server
from django.db.models import Q

# Create your views here.
def home(request):
    
    appsA = Apps.objects.filter(Patch_group='A')
    appsB = Apps.objects.filter(Patch_group='B')
    appsC = Apps.objects.filter(Patch_group='C')
    appsD = Apps.objects.filter(Patch_group='D')
    context = {'appsA':appsA , 'appsB':appsB, 'appsC':appsC, 'appsD':appsD}
    return render(request , 'home.html',context)


def app_info(request,pk):

    apps = Apps.objects.get(id=pk)
    server = apps.server_set.all()
    contacto = apps.contacts_set.all()
    bigIpp = apps.f5_set.all()

    context = {'apps':apps , 'server':server, 'contacto': contacto,'bigIpp':bigIpp }
    return render(request , 'app_info.html', context )

def search(request):
    match = ""
    if request.method=='GET':        
        search = request.GET.get('search')   
        print(search)    
        if search:
            match = Server.objects.filter( Q(ip__icontains=search)       |
                                           Q(hostname__icontains=search) |
                                           Q(app__mne__icontains=search) 
                                          )
            if match:
                return render(request , 'search.html',{'query':match})
            else:
                print("Match not found")
  


    
    return render(request , 'search.html')