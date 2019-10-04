from django.forms import ModelForm
from django import forms
from index.models import *


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
        label='Organization name',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",

            }
        )
    )
    Address = forms.CharField(
        label='Address',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )

    PR = forms.CharField(
        label='PR',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )
    Url = forms.CharField(
        label='URL',
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
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
        label='Contact Person',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",

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

    Region = forms.ChoiceField(
        choices=region_data,
        widget=forms.RadioSelect(
            attrs={
            }
        )
    )

    RegistrationDate = forms.DateField(
        label='Registration Date',
        widget=forms.DateInput(
            attrs={

                "class": "form-control datetimepicker",

            }
        )
    )
    Industry = forms.ModelMultipleChoiceField(
        queryset=Industry.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={

            }
        )
    )

    ServiceCategory = forms.ModelMultipleChoiceField(
        queryset=ServiceCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={

            }
        )
    )
