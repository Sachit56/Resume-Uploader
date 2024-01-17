from django import forms
from .models import ResumeModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model=ResumeModel
        fields="__all__"
        labels={'name':'Full Name','dob':'Date of Birth','gender':'Gender',
                'locality':'Locality','city':'City','pin':'Postal Code',
                'state':'State','mobile':'Mobile','email':'Email','job_city':'Job Location',
                'image':'Profile Picture','Upload your Resume':'file'}