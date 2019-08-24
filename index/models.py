from django.db import models
# Create your models here.

# Regions tuple added here
Region_data = (
    ('ada', 'Addis Adabba'),
    ('jhn', 'Johannesburg'),
    ('smt', 'Something')
)

class Industry(models.Model):
    Name = models.CharField(
        max_length=100,
        help_text="Enter the type of industry(eg. textile, metal)"
        )
    def __str__(self):
        return self.Name

class ServiceCategory(models.Model):
    Name = models.CharField(
        max_length=50,
        help_text="Enter the Name of service(eg. marketing, finance)"
        )
    def __str__(self):
        return self.Name

class OrgBaseInfo(models.Model):
    Name = models.CharField(max_length=100, help_text="Enter the name of Organisation(eg. Metal Industries)")
    Address = models.CharField(max_length=200, help_text="Enter the adress of the Organisation")
    RegistrationDate = models.DateField()
    Industry = models.ForeignKey('Industry', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    PR = models.CharField(max_length=300)
    Url = models.URLField(max_length=50)
    Affiliation = models.CharField(max_length=50)
    ContactPerson = models.CharField(max_length=50)
    Email = models.EmailField()
    Telephone = models.CharField(max_length=12, help_text="Enter the telephone number for the organisation")


    Region = models.CharField(
        max_length=3,
        choices=Region_data,
        blank=True,
        default='ada',
        help_text='Region of the company')

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name

class Service(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)
    Service = models.CharField(max_length=200)
    Contents = models.CharField(max_length=300)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

class Experience(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    Large = models.IntegerField()
    Medium = models.IntegerField()
    SmallandMicro = models.IntegerField()
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

class Case(models.Model):
    OrgName = models.ForeignKey('OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)
    Contents = models.CharField(max_length=300)
    Result = models.CharField(max_length=300)
    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)
