from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from home.forms import *
from django.contrib import messages
from home.filter import ListFilter
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage


# Create your views here.


def home(request):
    context = {'success': False}

    if request.method == 'POST':
        name = request.POST.get('examplename')
        number = request.POST.get('examplenumber')
        age = request.POST.get('exampleyears')
        gender = request.POST.get('examplegender')
        temp = request.POST.get('exampletemp')
        bp = request.POST.get('exampleB.P')
        pulserate = request.POST.get('examplepulserate')
        sugarf = request.POST.get('examplesugarf')
        sugarpp = request.POST.get('examplesugarpp')
        diagnosis = request.POST.get('examplediagnosis')
        medicine = request.POST.get('examplemedicine')
        reference = request.POST.get('examplereference')
        reports = request.FILES.getlist('file[]')

        #print(name, number, age, gender, temp, bp, pulserate,sugarf, sugarpp, diagnosis, medicine, reference)

        # for img in reports:
        #    fs=FileSystemStorage()
        #    file_path=fs.save(img.name,img)

        li = List(name=name, phonenumber=number, age=age, gender=gender, temp=temp, bp=bp,
                  pulserate=pulserate, sugarf=sugarf, sugarpp=sugarpp, diagnosis=diagnosis, medicine=medicine, reference=reference)
        li.save()
        for f in reports:
            fs = FileSystemStorage()
            file_path = fs.save(f.name, f)
            #image = Listimages(request.POST, request.FILES)
            image = Listimages(details=li, image=f)
            image.save()
        context = {'success': True}
        messages.info(request, "You successfully added the details")
        return render(request, 'index.html', context)
    else:
        context = {'success': False}

    return render(request, 'index.html', context)


def list(request):
    li = List.objects.all()
    #print(li)
    
    
   
    myFilter = ListFilter(request.GET, queryset=li)
    li = myFilter.qs

    context = {'list': li, 'myFilter': myFilter}
    return render(request, 'list.html', context)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('firstname')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        #print(username, password)
        if(user):
            auth.login(request, user)
            return render(request, 'index.html')

        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def edit(request, pk):
    det = List.objects.get(id=pk)
    #print(det)
    form = ListForm(instance=det)
    #im = ListImageForm(instance=det)
    #form1 = Listimages.objects.filter(details=det)
    if request.method == 'POST':
        form = ListForm(request.POST,  instance=det)
        #im = ListImageForm(request.POST, request.FILES, instance=det)
        
       # form1 = Listimages(request.POST, request.FILES, instance=det)
        if form.is_valid() :
            #form = ListForm(request.POST, request.FILES)
            #im=Listimages(request.POST,request.FILES)
            #print(form)
            form.save()
            #form1.save()
           # im.save()
            return render(request, 'index.html')

    context = {'form': form}
    return render(request, 'edit.html', context)


def delete(request, pk):
    det = List.objects.get(id=pk)
    #print(det)
    if request.method == 'POST':
        det.delete()
        return render(request, 'index.html')
        #return redirect('/')

    context = {'item': det}
    return render(request, 'delete.html', context)


def user_register(request):
    if(request.method == 'POST'):

        username = request.POST.get('username')

        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')
        if(password1 == password2):
            if(not User.objects.filter(username=username).exists()):
                user = User.objects.create_user(
                    username=username, password=password1)
                user.save()
                return render(request, 'login.html')

            else:
                messages.info(request, 'Username already registered')
                return render(request, 'register.html')
        else:
            messages.info(request, 'Password Mismatch')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return render(request, 'login.html')


def image(request,pk):
    im = List.objects.get(id=pk)
    
    form = Listimages.objects.filter(details=im)
    #print(form)

    context={'form':form}

    return render(request,'img.html',context)
