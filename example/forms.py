from django import forms
from .models import ResumeModel

Gender_Choices=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)

class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=Gender_Choices,widget=forms.RadioSelect)
    class Meta:
        model=ResumeModel
        fields="__all__"
        labels={'name':'Full Name','dob':'Date of Birth','gender':'Gender',
                'locality':'Locality','city':'City','pin':'Postal Code',
                'state':'State','mobile':'Mobile','email':'Email','job_city':'Job Location',
                'image':'Profile Picture','Upload your Resume':'file'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'job_city':forms.TextInput(attrs={'class':'form-control'}),
            }