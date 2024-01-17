from django.db import models

State_Choices = (
    ('Province 1', 'Province 1'),
    ('Province 2', 'Province 2'),
    ('Bagmati', 'Bagmati'),
    ('Gandaki', 'Gandaki'),
    ('Lumbini', 'Lumbini'),
    ('Karnali', 'Karnali'),
    ('Sudurpashchim', 'Sudurpashchim')
)



class ResumeModel(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=State_Choices,max_length=50)
    mobile=models.PositiveIntegerField()
    email=models.EmailField( max_length=254)
    job_city=models.CharField( max_length=50)
    image=models.ImageField(upload_to='images', height_field=None, width_field=None,blank=True)
    file=models.FileField(upload_to='files', max_length=100,blank=True)

    def __str__(self):
        return str(self.id)