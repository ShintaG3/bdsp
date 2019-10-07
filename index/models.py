from django.db import models
from django.urls import reverse
# Create your models here.

# Regions tuple added here
Region_data = (
    ('Addis Ababba', 'Addis Ababba'),
    ('Johannesburg', 'Johannesburg'),
    ('Something', 'Something')
)


class Industry(models.Model):
    Name = models.CharField(
        max_length=100,
        #help_text="Enter the type of industry(eg. textile, metal)"
    )

    def __str__(self):
        return self.Name


class ServiceCategory(models.Model):
    Name = models.CharField(
        max_length=50,
        #help_text="Enter the Name of service(eg. marketing, finance)"
    )

    def __str__(self):
        return self.Name


class OrgBaseInfo(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    RegistrationDate = models.DateField()
    Industry = models.ManyToManyField('Industry')
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    PR = models.CharField(max_length=300)
    Url = models.URLField(max_length=50)
    Affiliation = models.CharField(max_length=50)
    ContactPerson = models.CharField(max_length=50)
    Email = models.EmailField()
    Telephone = models.CharField(max_length=12)

    Region = models.CharField(
        max_length=30,
        choices=Region_data,
        blank=True
    )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name

    def get_absolute_url(self):
        return reverse('details', args=[self.id])


class Service(models.Model):
    OrgName = models.ForeignKey(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    Service = models.CharField(max_length=200)
    Contents = models.CharField(max_length=300)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])


class Experience(models.Model):
    OrgName = models.OneToOneField(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    Large = models.IntegerField()
    Medium = models.IntegerField()
    SmallandMicro = models.IntegerField()

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])


class Case(models.Model):
    OrgName = models.ForeignKey(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    # ServiceCategory = models.ForeignKey(
    #     'ServiceCategory', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    Contents = models.CharField(max_length=300)
    Result = models.CharField(max_length=300)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])
