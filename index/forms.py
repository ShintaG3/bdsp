from django.forms import ModelForm
from django import forms
from index.models import *
from django.contrib.auth.forms import AuthenticationForm

def region_data():
    return Region_data


#---Login---#
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password'
        }
    ))

#---Search---#
class SearchForm(forms.Form):
    search = forms.CharField(max_length=15, min_length=1)


# ---Industry---#
class IndustryForm(ModelForm):
    class Meta:
        model = Industry
        fields = ['Name']

    Name = forms.CharField(
        label='Industry',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

# ---Organization---#
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
        required=False,
        label='Address',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 1
            }
        )
    )

    PR = forms.CharField(
        required=False,
        label='PR',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 8
            }
        )
    )

    Url = forms.CharField(
        required=False,
        label='URL',
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    Affiliation = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    OfficeHour = forms.CharField(
        required=False,
        label="Business Hour",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    ContactPerson = forms.CharField(
        required=False,
        label='Contact Person',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",

            }
        )
    )

    Email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    Telephone = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
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
        required=False,
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
        )
    )

    ServiceCategory = forms.ModelMultipleChoiceField(
        queryset=ServiceCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(
        )
    )

    TargetCompanySize = forms.ModelMultipleChoiceField(
        required=False,
        queryset = TargetCompanySize.objects.all(),
        widget = forms.CheckboxSelectMultiple(

        )
    )

#---Service---
class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['ServiceCategory', 'Service', 'Contents']

    ServiceCategory = forms.ModelMultipleChoiceField(
        label='Service Category',
        queryset=ServiceCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(
        )
    )

    Service = forms.CharField(
        required=False,
        label='Title',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )
    Contents = forms.CharField(
        required=False,
        label='Contents',
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )


class addServiceCategoryForm(ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ['Name']
    Name = forms.CharField(
        label="Service Category",
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

#---Experience---
class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['Year', 'Large', 'Medium', 'SmallandMicro']

    Year = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    Large = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    Medium = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    SmallandMicro = forms.IntegerField(
        label='Small & Micro',
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
            }
        )
    )


#---Case---
class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = ['ServiceCategory', 'Result', 'Contents']

    ServiceCategory = forms.ModelMultipleChoiceField(
        queryset=ServiceCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(
        )
    )

    Contents = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )

    Result = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                'rows': 3
            }
        )
    )
