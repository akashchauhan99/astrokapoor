from django.db import models

# Create your models here.

class Category(models.Model):
    Title = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.Title
    
class Seller(models.Model):
    Title = models.CharField(default="", max_length=100)
    Image = models.ImageField(upload_to='sellerimages/')

    def __str__(self):
        return self.Title

class CategoryService(models.Model):
    Title = models.CharField(default="", max_length=100)
    Amount = models.FloatField()
    Image = models.ImageField(upload_to='customerserviceimages/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.Title

class Birth(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    MARITALSTATUS = (
        ('Married', 'Married'),
        ('UnMarried', 'UnMarried')
    )
    Name = models.CharField(default="", max_length=100)
    Gender = models.CharField(max_length=10 ,choices=GENDER)
    Marital_Status = models.CharField(max_length=15 ,choices=MARITALSTATUS)
    Date_of_birth = models.DateField()
    Time = models.TimeField()
    Country_of_birth = models.CharField(default="", max_length=100)
    State_of_birth = models.CharField(default="", max_length=100)
    Place_of_birth = models.CharField(default="", max_length=100)
    Longitude = models.CharField(default="", max_length=100)
    Latitude = models.CharField(default="", max_length=100)

    def __str__(self):
        return self.Name

class ContactDetail(models.Model):
    Email = models.EmailField(max_length=200, default="")
    Mobile = models.CharField(default="", max_length=20)
    Address = models.CharField(max_length=150, default="")
    Question = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.Email 





