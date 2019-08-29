from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Industry, ServiceCategory, Region_data, OrgBaseInfo, Service, Case, Experience
from django.urls import reverse

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

def getregion(query_result):
    for query in query_result:
        for region in Region_data:
            if region[0] == query.Region:
                query.Region = region[1]

def list (request):
    if request.method == 'POST':
        regions = request.POST.getlist('region')
        print(regions)
        industries = request.POST.getlist('industry')
        services = request.POST.getlist('service')

    # Send empty if nothing selected
        if len(regions)==0 and len(industries)==0 and len(services)==0:
            context = {
            }
            return render(request, 'index/list.html', context=context)

    #chaining the  input data for querying
        if len(regions) == 0 or "allregion" in regions:
            print("working")
            for region in Region_data:
                regions.append(region[0])

        if len(industries) == 0 or "allindustries" in industries:
            allindustries = Industry.objects.all()
            for industry in allindustries:
                industries.append(industry.Name)

        if len(services) == 0 or "allservices" in services:
            allservices = ServiceCategory.objects.all()
            for service in allservices:
                services.append(service.Name)

        query_result = OrgBaseInfo.objects.filter(
            Region__in=regions, Industry__Name__in=industries, ServiceCategory__Name__in=services).distinct()
        getregion(query_result)
        context = {
            'query_result': query_result
        }
        return render(request, 'index/list.html', context=context)
    query_result = OrgBaseInfo.objects.all()
    getregion(query_result)
    context = {
        'query_result': query_result
        }
    return render(request, 'index/list.html', context=context)

def details (request, id):
    org = OrgBaseInfo.objects.get(pk=id)
    region = org.Region
    for r in Region_data:
        if r[0] == region:
            region = r[1]
        org.Region = region
    services = Service.objects.filter(OrgName=org)
    cases = Case.objects.filter(OrgName=org)
    experiences = Experience.objects.filter(OrgName=org)
    context={
    'org': org,
    'services': services,
    'cases': cases,
    'experiences': experiences
    }
    return render(request, 'index/details.html', context=context)

def editPage(request, id):
    if request.method == 'POST':
        orgid = int(request.session.get('orgid'))
        org = OrgBaseInfo.objects.get(pk=orgid)
        name = request.POST.get("Name")
        address = request.POST.get("Address")
        telephone = request.POST.get("Telephone")
        regiondata = request.POST.get("changeregion")
        industrydata = request.POST.get("changeindustry")
        industry = Industry.objects.get(Name=industrydata)
        newservicesdata = request.POST.getlist('Services')
        PR = request.POST.get('PR')
        registrationDate = request.POST.get("RegistrationDate")
        Affiliation = request.POST.get('Affiliation')
        URL = request.POST.get('URL')
        ContactPerson = request.POST.get('ContactPerson')
        Email = request.POST.get('Email')
        for region in Region_data:
            if regiondata == Region_data[1]:
                regiondata = Region_data[0]
        # Update the Organisation information
        OrgBaseInfo.objects.filter(pk=orgid).update(
        Name=name, Address=address, Region=regiondata,
        RegistrationDate=registrationDate, Industry=industry, PR=PR, Email=Email, Affiliation=Affiliation,
        Url=URL, ContactPerson=ContactPerson, Telephone=telephone)
        #Delete the existing services
        oldServices = org.ServiceCategory.all()
        for service in oldServices:
            org.ServiceCategory.remove(service)
        # Adding the services
        for service in newservicesdata:
            addservice = ServiceCategory.objects.get(Name=service)
            org.ServiceCategory.add(addservice)
        return redirect('details', id=int(orgid))
    org = OrgBaseInfo.objects.get(pk=id)
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
    # Get the regions
    currentregion = org.Region
    otherregions = []
    for region in Region_data:
        if region[0] != currentregion:
            otherregions.append(region[1])
    for region in Region_data:
        if currentregion == region[0]:
            currentregion = region[1]
    allservices = Service.objects.all()
    currentindustry = org.Industry.Name
    allindustries = Industry.objects.all()
    otherindustries = []
    for industry in allindustries:
        if industry.Name != currentindustry:
            otherindustries.append(industry.Name)
    context={
        'currentregion': currentregion,
        'otherregions': otherregions,
        'org': org,
        'checked': checked,
        'unchecked': unchecked,
        'currentindustry': currentindustry,
        'otherindustries': otherindustries
    }
    request.session['orgid'] = org.id
    return render(request, 'index/edit.html', context=context)

def search(request):
    orgInfo = request.POST["orgInfo"]
    orgs = OrgBaseInfo.objects.filter(Name__icontains=orgInfo)
    return render(request,'index/list.html',context={'query_result':orgs})

def editexperiences(request, id):
    org = OrgBaseInfo.objects.get(pk=id)
    experiences = Experience.objects.filter(OrgName=org).first()
    if request.method == 'POST':
        large = request.POST.get('Large')
        medium = request.POST.get('Medium')
        smallandmicro = request.POST.get('SmallandMicro')
        experiences.Large = int(large)
        experiences.Medium = int(medium)
        experiences.SmallandMicro = int(smallandmicro)
        experiences.save()
        return redirect('details', id=int(id))
    context = {
        'experiences': experiences
        }
    return render(request, 'index/edit_experiences.html', context=context)

def editcases(request, id):
    org = OrgBaseInfo.objects.get(pk=id)
    cases = Case.objects.filter(OrgName=org)
    if request.method == 'POST':
        service = request.POST.get("ServiceCategory")
        print(service)
        ServiceCat = ServiceCategory.objects.get(Name=service)
        contents = request.POST.get("Contents")
        result = request.POST.get("Result")
        caseid = request.POST.get("case")
        case = Case.objects.get(pk=int(caseid))
        case.OrgName=org
        case.ServiceCategory=ServiceCat
        case.Contents=contents
        case.Result=result
        case.save()
        return redirect('details', id=id)
    context = {
        'cases': cases,
        'services': ServiceCategory.objects.all()
        }
    return render(request, 'index/edit_cases.html', context=context)

def editservices(request, id):
    org = OrgBaseInfo.objects.get(pk=id)
    services = Service.objects.filter(OrgName=org)
    context = {
        'services': services
        }
    return render(request, 'index/edit_services.html', context=context)
