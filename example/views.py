from .forms import ResumeForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_list_or_404
from .models import ResumeModel

class Home(View):
    def get(self,request):
        form=ResumeForm()
        candidates=ResumeModel.objects.all()

        return render(request,'example/home.html',{
            'form':form,
            'candidates':candidates
        })
    def post(self,request):
        if request.POST:
            form=ResumeForm(request.POST,request.FILES)

            if form.is_valid():
                form.save()
                print('Sucess!')
            return redirect('/')  
        return render(request,'example/home.html',{
            'form':form
        })        


class CandidateView(View):
    def get(self,request,pk):
        candidate=get_list_or_404(ResumeModel,pk=pk)
        return render(request,'example/candidate.html',{
            'candidates':candidate
        })
