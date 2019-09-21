from django.forms import ModelForm
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
