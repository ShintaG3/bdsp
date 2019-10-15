from django.db import models
from django.urls import reverse

# Regions tuple added here
Region_data = (
    ('Addis Ababba', 'Addis Ababba'),
    ('Afar', 'Afar'),
    ('Amhara', 'Amhara'),
    ('Benishangul-Gumuz', 'Benishangul-Gumuz'),
    ('Dire Dawa', 'Dire Dawa'),
    ('Gambela', 'Gambela'),
    ('Harari', 'Harari'),
    ('Oromia', 'Oromia'),
    ('Somali', 'Somali'),
    ('Tigray', 'Tigray'),
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
    Address = models.CharField(max_length=1000, null=True, blank=True)
    RegistrationDate = models.DateField(null=True, blank=True)
    Industry = models.ManyToManyField('Industry')
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    PR = models.CharField(max_length=2000, null=True, blank=True)
    Url = models.URLField(max_length=256, null=True, blank=True)
    Affiliation = models.CharField(max_length=50, null=True, blank=True)
    ContactPerson = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Telephone = models.CharField(max_length=100, null=True, blank=True)
    OfficeHour = models.CharField(max_length=100, null=True, blank=True)
    Region = models.CharField(max_length=50, choices=Region_data, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.Name

    def get_absolute_url(self):
        return reverse('details', args=[self.id])


class Service(models.Model):
    OrgName = models.ForeignKey(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    Service = models.CharField(max_length=2000, null=True, blank=True)
    Contents = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])


class Experience(models.Model):
    OrgName = models.OneToOneField(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    Large = models.IntegerField(null=True, blank=True)
    Medium = models.IntegerField(null=True, blank=True)
    SmallandMicro = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])


class Case(models.Model):
    OrgName = models.ForeignKey(
        'OrgBaseInfo', on_delete=models.SET_NULL, null=True)
    ServiceCategory = models.ManyToManyField('ServiceCategory')
    Contents = models.CharField(max_length=2000, null=True, blank=True)
    Result = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return str(self.OrgName)

    def get_absolute_url(self):
        Orgid = self.OrgName.id
        return reverse('details', args=[str(Orgid)])
