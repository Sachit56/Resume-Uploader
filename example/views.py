from .forms import ResumeForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

class Home(View):
    def get(self,request):
        form=ResumeForm()

        return render(request,'example/home.html',{
            'form':form
        })