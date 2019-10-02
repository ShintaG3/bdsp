from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


def index(request):
    regiondata = []
    for region in Region_data:
        regiondata.append(region[0])
    context = {
        'industries': Industry.objects.all(),
        'services': ServiceCategory.objects.all(),
        'regions': regiondata
    }
    return render(request, 'index/index.html', context=context)


def list(request):
    if request.method == 'POST':
        regions = request.POST.getlist('region')
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')
    # Send empty if nothing selected
        if len(regions) == 0 and len(industries) == 0 and len(services) == 0:
            context = {
            }
            return render(request, 'index/list.html', context=context)

    # chaining the  input data for querying
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
            Q(Region__in=regions) & Q(Industry__Name__in=industries) & Q(
                ServiceCategory__Name__in=services)
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


def details(request, id):
    org = get_object_or_404(OrgBaseInfo, pk=id)
    region = org.Region
    services = Service.objects.filter(OrgName=org)
    cases = Case.objects.filter(OrgName=org)
    experiences = Experience.objects.filter(OrgName=org)
    context = {
        'org': org,
        'services': services,
        'cases': cases,
        'experiences': experiences
    }
    return render(request, 'index/details.html', context=context)


def search(request):
    orgInfo = request.POST["orgInfo"]
    orgs = OrgBaseInfo.objects.filter(
        Name__icontains=orgInfo).order_by('Region')
    return render(request, 'index/list.html', context={'query_result': orgs})


class ServiceCreate(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm


class ServiceUpdate(LoginRequiredMixin, UpdateView):
    model = Service
    #fields = ['ServiceCategory', 'Service', 'Contents']
    form_class = ServiceForm


@login_required
def ServiceDelete(request, pk):
    service = Service.objects.get(id=pk)
    org = OrgBaseInfo.objects.get(Name=service.OrgName)
    service.delete()
    return redirect('details', id=int(org.id))


class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    #fields = '__all__'
    form_class = CaseForm


class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    #fields = ['ServiceCategory', 'Contents', 'Result']
    form_class = CaseForm


@login_required
def CaseDelete(request, pk):
    case = Case.objects.get(id=pk)
    org = OrgBaseInfo.objects.get(Name=case.OrgName)
    case.delete()
    return redirect('details', id=int(org.id))


class ExperienceCreate(LoginRequiredMixin, CreateView):
    model = Experience
    form_class = ExperienceForm
    #fields = '__all__'


class ExperienceUpdate(LoginRequiredMixin, UpdateView):
    model = Experience
    #fields = ['Large', 'Medium', 'SmallandMicro']
    form_class = ExperienceForm


class ExperienceDelete(LoginRequiredMixin, DeleteView):
    model = Experience
    success_url = reverse_lazy('index')

# Registration of New Org:


class OrgbaseInfoCreate(LoginRequiredMixin, CreateView):
    model = OrgBaseInfo
    form_class = OrgBaseInfoForm
    # success_url = reverse_lazy('index')


class OrgBaseInfoUpdate(LoginRequiredMixin, UpdateView):
    model = OrgBaseInfo
    form_class = OrgBaseInfoForm
    context_object_name = 'org'
    template = 'orgbaseinfor_form.html'

    def get_success_url(self):
        id = self.kwargs['pk']
        print(id)
        return reverse_lazy('details', kwargs={'id': id})
