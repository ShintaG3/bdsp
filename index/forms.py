from django.forms import ModelForm
from django import forms
from index.models import OrgBaseInfo, Service, Experience, Case, Industry, Region_data

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = '__all__'
    Large = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Experience with Large Organisations"
            }
        )
    )
    Medium = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Experience with Medium Organisations"
            }
        )
    )
    SmallandMicro = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Experience with Small and Micro Organisations"
            }
        )
    )


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
    Service = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Service Provides",
                'rows': 3
            }
        )
    )
    Contents = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Summary for the Serice provides",
                'rows': 3
            }
        )
    )

class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
    Result = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Result",
                'rows': 3
            }
        )
    )
    Contents = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Contents",
                'rows': 3
            }
        )
    )

def region_data():
    return Region_data

class OrgBaseInfoForm(ModelForm):
    class Meta:
        model = OrgBaseInfo
        fields = '__all__'
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Name of Organisation"
            }
        )
    )
    Address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Address of Organisation",
                'rows': 3
            }
        )
    )

    PR = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "PR of Organisation",
                'rows': 3
            }
        )
    )
    Url = forms.CharField(
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "URL of Organisation"
            }
        )
    )
    Affiliation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Affiliation of Organisation"
            }
        )
    )
    ContactPerson = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Contact Person for the Organisation"
            }
        )
    )
    Email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email for the Organisation"
            }
        )
    )
    Telephone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Telephone Number"
            }
        )
    )
    Region = forms.ChoiceField(choices= region_data,
        widget=forms.RadioSelect(
            attrs={

            }
        )
    )
