from django.shortcuts import render
from django.http import HttpResponse
from .models import Industry, ServiceCategory, Region_data, OrgBaseInfo

def index (request):

    if request.method == 'POST':
        regions = request.POST.getlist('region')
        print(regions)
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')
        # Send all the data if any all is selected
        if "allregion" in regions or "allindustries" in industries or "allservices" in services:
            query_result = OrgBaseInfo.objects.all()
            print(query_result)
            return HttpResponse(query_result)
        if len(regions)==0 and len(industries)==0 and len(services)==0:
            return HttpResponse('No result')
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
        query_result = OrgBaseInfo.objects.filter(Region__in=regions, Industry__Name__in=industries, ServiceCategory__Name__in=services).distinct()
        print(query_result)
        return HttpResponse(query_result)
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

def organization (request):
    return render(request, 'index/organization.html')

def service (request):
    return render(request, 'index/service.html')

def detail (request):
    return render(request, 'index/detail.html')
