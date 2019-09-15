from django.test import TestCase
import datetime
from django.utils import timezone
# Create your tests here.

from index.models import OrgBaseInfo, ServiceCategory, Industry

class OrgBaseInfoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        org = OrgBaseInfo(
        Name="Advaita Sol.",
        Address="type-IV/15, Sector 15, Kapporthala, Lucknow",
        Region='ada',
        RegistrationDate=timezone.now(),
        PR="none",
        Email="vikassrinitb@gmail.com",
        Affiliation="None",
        Url="vikassrinitb.com",
        ContactPerson="vikas",
        Telephone="9205731743")
        org.save()
        service1 = ServiceCategory.objects.create(
            Name = "Managment"
        )
        service2 = ServiceCategory.objects.create(
            Name = "Finance"
        )
        service3 = ServiceCategory.objects.create(
            Name = "Marketing"
        )
        industry1 = Industry.objects.create(
            Name = "Metal"
        )
        industry2 = Industry.objects.create(
            Name = "textile"
        )
        industry3 = Industry.objects.create(
            Name = "dairy"
        )
        org = OrgBaseInfo.objects.get(id=1)
        org.ServiceCategory.add(service1)
        org.ServiceCategory.add(service2)
        org.Industry.add(industry1)
        org.Industry.add(industry2)


    def test_name_label(self):
        #author=Author.objects.get(id=1)
        #field_label = author._meta.get_field('first_name').verbose_name
        #self.assertEquals(field_label,'first name')
        org1 = OrgBaseInfo.objects.get(id=1)
        field_label = org1._meta.get_field('Name').verbose_name
        self.assertEquals(field_label,'Name')

    def test_registration_date_label(self):
        org1 = OrgBaseInfo.objects.get(id=1)
        field_label = org1._meta.get_field('RegistrationDate').verbose_name
        self.assertEquals(field_label,'RegistrationDate')

    def test_name_max_length(self):
        org1 = OrgBaseInfo.objects.get(id=1)
        max_length = org1._meta.get_field('Name').max_length
        self.assertEquals(max_length,100)


    def test_get_absolute_url(self):
        org1 = OrgBaseInfo.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(org1.get_absolute_url(),'/details/1')
