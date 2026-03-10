from django.db import models

# Create your models here.

class Departments(models.Model):
    dep_name=models.CharField(max_length=50)
    dep_description=models.TextField()

    def __str__(self):
         return self.dep_name

   

class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=200)
    dep_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    def __str__(self):
        return'DR'+ self.doc_name +'-('+ self.doc_spec+')'
    # # image=models.ImageField(upload_to='doctors') #pillow library for image

class Booking(models.Model):
    pname= models.CharField(max_length=50)
    pphone=models.IntegerField()
    eemail=models.EmailField()
    docname=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    bookingdate=models.DateField()
    bookedon=models.DateField(auto_now=True)



