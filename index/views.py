from django.shortcuts import render
from django.http import HttpResponse
from .models import Industry, ServiceCategory, Region_data, OrgBaseInfo, Service

def index (request):
    regiondata = Region_data
    regions = []
    for region in regiondata:
        regions.append({'name':region[0], 'value':region[1]})
    context = {
        'industries': Industry.objects.all(),
        'services': ServiceCategory.objects.all(),
        'regions': regions
    }
    return render(request, 'index/index.html', context=context)

def list (request):
    if request.method == 'POST':
        regions = request.POST.getlist('region')
        print(regions)
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')
    # Send all the data if any all is selected
        if "allregion" in regions or "allindustries" in industries or "allservices" in services:
            query_result = OrgBaseInfo.objects.all()
            context = {
                'query_result': query_result
            }
            return render(request, 'index/list.html', context=context)
    # Send empty if nothing selected
        if len(regions)==0 and len(industries)==0 and len(services)==0:
            context = {
            }
            return render(request, 'index/list.html', context=context)
    #chaining the  input data for querying
        if len(regions) == 0:
            for region in Region_data:
                regions.append(region[0])
            print('no region',regions)
        if len(industries) == 0:
            allindustries = Industry.objects.all()
            for industry in allindustries:
                industries.append(industry.Name)
            print('no industry',industries)
        if len(services) == 0 :
            allservices = ServiceCategory.objects.all()
            for service in allservices:
                services.append(service.Name)
            print('no service')
        query_result = OrgBaseInfo.objects.filter(
            Region__in=regions, Industry__Name__in=industries, ServiceCategory__Name__in=services).distinct()
        context = {
            'query_result': query_result
        }
        return render(request, 'index/list.html', context=context)
    query_result = OrgBaseInfo.objects.all()
    context = {
        'query_result': query_result
        }
    return render(request, 'index/list.html', context=context)

def details(request, name):
    org = OrgBaseInfo.objects.get(Name=name)
    region = org.Region
    for r in Region_data:
        if r[0] == region:
            region = r[1]
        org.Region = region
    services = Service.objects.filter(OrgName=org)
    print(services)
    context={
    'org': org,
    'services': services
    }
    return render(request, 'index/details.html', context=context)

def editPage(request, name):
    if request.method == 'POST':
        ind = request.POST["changeindustry"]
        context = {
        'industry': request.POST["changeindustry"],
        'services': request.POST.getlist('Services'),
        'PR': request.POST.get('PR'),
        'RegistrationDate': request.POST.get('RegistrationDate'),
        'URL': request.POST.get('URL'),
        'ContactPerson': request.POST.get('ContactPerson'),
        'Email': request.POST.get('Email')
        }
        return HttpResponse(context['industry'])
    org = OrgBaseInfo.objects.get(Name=name)
    # Get the services for this Org
    checked = []
    checkedServices = org.ServiceCategory.all()
    for service in checkedServices:
        checked.append(service.Name)
    allServices = []
    for service in ServiceCategory.objects.all():
        allServices.append(service.Name)
    unchecked = []
    for service in allServices:
        if service not in checked:
            unchecked.append(service)
    allservices = Service.objects.all()
    currentindustry = org.Industry.Name
    allindustries = Industry.objects.all()
    otherindustries = []
    for industry in allindustries:
        if industry.Name != currentindustry:
            otherindustries.append(industry.Name)
    context={
    'org': org,
    'checked': checked,
    'unchecked': unchecked,
    'currentindustry': currentindustry,
    'otherindustries': otherindustries
    }
    return render(request, 'index/edit.html', context=context)
