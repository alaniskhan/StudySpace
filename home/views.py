
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import Material
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    materials = Material.objects.all()
    return render(request, 'index.html', {'materials':materials, 'request': request})


def create(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        name = request.POST['chapterName']
        video_url = request.POST['videoUrl']
        file = request.FILES.get('pdfFile', None)
        if file is not None:
            fs.save(file.name, file)
            
        img = request.FILES.get('imgFile', None)
        if img is not None:
            fs.save(img.name, img)
        material = Material(name=name, file=file, video_url=video_url, img=img)

        material.save()

        return redirect('/')
    else:
        return render(request, 'create.html')


def view_login(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else: 
            
            return redirect('/login/')
    else: 
        return render(request, 'login.html')

def view_logout(request):
    logout(request)
    return redirect('/')


def search(request):
    if request.method == "GET":
        search = request.GET['search-chapter']
        finds = Material.objects.filter(name__contains=search)
        print(finds)
        return render(request, 'search.html', {'finds' : finds})
    else:
        return render(request, 'search.html')

def delete(request, id):
    singleFile = Material.objects.get(id=id)
    singleFile.delete()
    return redirect('/')

def edit(request, id):
    singleFile = Material.objects.get(id=id)
    return render(request, 'edit.html', {'request': request, 'singleFile': singleFile})


def editrecord(request, id):
    if request.method == 'POST':
        fs = FileSystemStorage()
        name = request.POST['chapterName']
        video_url = request.POST['videoUrl']
        file = request.FILES.get('pdfFile', None)
        if file is not None:
            fs.save(file.name, file)
            
        img = request.FILES.get('imgFile', None)
        if img is not None:
            fs.save(img.name, img)
        
        single = Material.objects.get(id=id)

        single.name = name
        single.video_url = video_url
        single.file = file
        single.img = img

        single.save()

        return redirect('/')