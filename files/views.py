from django.shortcuts import render  
from django.http import HttpResponse  
from .functions import handle_uploaded_file  
from .forms import FileForm


def home(request):
    return render(request, 'files/home.html', {})


def upload(request):  
    if request.method == 'POST':  
        uploaded_file = FileForm(request.POST, request.FILES)  
        if uploaded_file.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return render(request, "files/success.html", {}) 
        return render(request, "files/ohno.html", {})
      
    cnab_file = FileForm()  
    return render(request,"files/upload.html",{'form': cnab_file}) 


def upload_success(request):
    return render(request, 'files/success.html', {})