from django.db import models

# Create your models here.

class Industry(models.Model):
    Name = models.CharField(
        max_length=200,
        help_text="Enter the type of industry(eg. textile, metal)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name

class ServiceCategory(models.Model):
    Name = models.CharField(
        max_length=200,
        help_text="Enter the Name of service(eg. marketing, finance)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name

class OrgBaseInfo(models.Model):
    Name = models.CharField(max_length=200, help_text="Enter the name of Organisation(eg. Metal Industries)")
    Address = models.CharField(max_length=500, help_text="Enter the adress of the Organisation")
    RegistrationDate = models.DateField()
    Industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)
    PR = models.CharField(max_length=500)
    Url = models.CharField(max_length=100)
    Affiliation = models.CharField(max_length=50)
    ContactPerson = models.CharField(max_length=50)
    Email = models.EmailField()
    Telephone = models.CharField(max_length=12, help_text="Enter the telephone number for the organisation")

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name, self.Address

class Service(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo')
    ServiceCategory = models.ForeignKey('ServiceCategory')
    Service = models.CharField(max_length=200)
    Contents = models.CharField(max_length=500)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.OrgName, self.Service

class Experience(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo')
    Large = models.IntegerField()
    Medium = models.IntegerField()
    SmallandMicro = models.IntegerField()
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.OrgName, self.Large, self.Medium, self.SmallandMicro

class Case(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo')
    ServiceCategory = models.ForeignKey('ServiceCategory')
    Contents = models.CharField(max_length=200)
    Result = models.CharField(max_length=500)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.OrgName, self.Result
