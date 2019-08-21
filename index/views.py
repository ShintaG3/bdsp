from django.shortcuts import render
from django.http import HttpResponse
from .models import Industry, ServiceCategory, Region_data, OrgBaseInfo

def index (request):
    if request.method == 'POST':
        regions = request.POST.getlist('region')
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')
        service_name = []
        industry_name = []
        region_name = []

        if services:
            for service in services:
                service_name.append(ServiceCategory.objects.get(Name=service).Name)
        if industries:
            for industry in industries:
                industry_name.append(Industry.objects.get(Name=industry).Name)
                print(industry_name)
        if regions:
            for region in regions:
                for Region in Region_data:
                    if region == Region[1]:
                        region_name.append(Region[0])
        if "allregion" in regions:
            query_result = OrgBaseInfo.objects.all()
            print(query_result)
            return render(request, 'index/index.html')
        print(region_name,)
        query_result = OrgBaseInfo.objects.filter(Region__in=region_name, Industry__Name__in=industry_name, ServiceCategory__Name__in=service_name)
        print(query_result)
        return render(request, 'index/index.html')
    regiondata = Region_data
    regions = []
    for region in regiondata:
        regions.append(region[1])
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
