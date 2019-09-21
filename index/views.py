from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Industry, ServiceCategory, Region_data, OrgBaseInfo, Service, Case, Experience
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def index (request):
    regiondata = []
    for region in Region_data:
        regiondata.append(region[0])
    context = {
        'industries': Industry.objects.all(),
        'services': ServiceCategory.objects.all(),
        'regions': regiondata
    }
    return render(request, 'index/index.html', context=context)

def list (request):
    if request.method == 'POST':
        regions = request.POST.getlist('region')
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')
    # Send empty if nothing selected
        if len(regions)==0 and len(industries)==0 and len(services)==0:
            context = {
            }
            return render(request, 'index/list.html', context=context)

    #chaining the  input data for querying
        if len(regions) == 0:
            for region in Region_data:
                regions.append(region[0])

        if len(industries) == 0:
            allindustries = Industry.objects.all()
            for industry in allindustries:
                industries.append(industry.Name)

        if len(services) == 0:
            allservices = ServiceCategory.objects.all()
            for service in allservices:
                services.append(service.Name)
    # Query Codes here
        query_result = OrgBaseInfo.objects.filter(
        Q(Region__in=regions) & Q(Industry__Name__in=industries) & Q(ServiceCategory__Name__in=services)
        ).distinct().order_by('Region')
        context = {
            'query_result': query_result
        }
        return render(request, 'index/list.html', context=context)
    query_result = OrgBaseInfo.objects.all()
    context = {
        'query_result': query_result
        }
    return render(request, 'index/list.html', context=context)

def details (request, id):
    org = get_object_or_404(OrgBaseInfo, pk=id)
    region = org.Region
    services = Service.objects.filter(OrgName=org)
    cases = Case.objects.filter(OrgName=org)
    experiences = Experience.objects.filter(OrgName=org)
    context={
    'org': org,
    'services': services,
    'cases': cases,
    'experience': experiences
    }
    return render(request, 'index/details.html', context=context)



def search(request):
    orgInfo = request.POST["orgInfo"]
    orgs = OrgBaseInfo.objects.filter(Name__icontains=orgInfo).order_by('Region')
    return render(request,'index/list.html',context={'query_result':orgs})

from django.urls import reverse_lazy

class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    fields = '__all__'

class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    fields = ['ServiceCategory', 'Service', 'Contents']

class ServiceDelete(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('index')

class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['ServiceCategory', 'Contents', 'Result']

class CaseDelete(LoginRequiredMixin,DeleteView):
    model = Case
    success_url = reverse_lazy('index')

class ExperienceCreate(LoginRequiredMixin,CreateView):
    model = Experience
    fields = '__all__'

class ExperienceUpdate(UpdateView):
    model = Experience
    fields = ['Large', 'Medium', 'SmallandMicro']

class ExperienceDelete(DeleteView):
    model = Experience
    success_url = reverse_lazy('index')

# Registration of New Org:
class OrgbaseInfoCreate(LoginRequiredMixin, CreateView):
    model = OrgBaseInfo
    fields = '__all__'

class OrgBaseInfoUpdate(LoginRequiredMixin, UpdateView):
    model = OrgBaseInfo
    fields = '__all__'
