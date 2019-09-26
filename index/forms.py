from django.forms import ModelForm
from django import forms
from index.models import OrgBaseInfo, Service, Experience, Case


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['OrgName']


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'


class OrgBaseInfoForm(ModelForm):
    class Meta:
        model = OrgBaseInfo
        fields = '__all__'

    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Name"
            }
        )
    )

    # models.CharField(
    #     max_length=100, help_text="Enter the name of Organisation(eg. Metal Industries)")
    # Address = models.CharField(
    #     max_length=200, help_text="Enter the adress of the Organisation")
    # RegistrationDate = models.DateField()
    # Industry = models.ManyToManyField('Industry')
    # ServiceCategory = models.ManyToManyField('ServiceCategory')
    # PR = models.CharField(max_length=300)
    # Url = models.URLField(max_length=50)
    # Affiliation = models.CharField(max_length=50)
    # ContactPerson = models.CharField(max_length=50)
    # Email = models.EmailField()
    # Telephone = models.CharField(
    #     max_length=12, help_text="Enter the telephone number for the organisation")

    # Region = models.CharField(
    #     max_length=30,
    #     choices=Region_data,
    #     blank=True,
    #     default='ada',
    #     help_text='Region of the company')
