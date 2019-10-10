from django.test import TestCase
import datetime
from django.utils import timezone
from django.urls import reverse, resolve
from django.test import Client
from .views import *
# Create your tests here.
from index.models import *
from django.contrib.auth.models import User

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
        #org = OrgBaseInfo.objects.get(id=1)
        org.ServiceCategory.add(service1)
        org.ServiceCategory.add(service2)
        org.Industry.add(industry1)
        org.Industry.add(industry2)

        case1 = Case(
        OrgName=org,
        ServiceCategory=service1,
        Contents='Nothing Much!',
        Result='NC'
        )
        case1.save()


    def test_name_label(self):
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

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list'))
        self.assertTemplateUsed(response, 'index/list.html')

    def test_details_view_status_code(self):
        url = reverse('details', kwargs={'id':1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_details_view_status_not_found_code(self):
        url = reverse('details', kwargs={'id':100})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_details_url_resolves_home_view(self):
        view = resolve('/details/1')
        self.assertEquals(view.func, details)

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)

    def test_list_view_status_code(self):
        url = reverse('list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/list')
        self.assertEquals(view.func, list)

class CheckAuthenticationForEditTest(TestCase):
    @classmethod
    def setup(self):
        test_user1 = User.objects.create_user(username="monusri", password="hellyeah@2019")
        test_user2 = User.objects.create_user(username="sonusri", password="hellyeah@2019@montevideo")
        #test_user1.user_permissions.add(permission)
        test_user1.save()
        test_user2.save()

    def test_edit_page_redirect_if_not_logged_in(self):
        response = self.client.get('/editPage/1')
        self.assertRedirects(response, '/accounts/login/?next=/editPage/1')

    def test_edit_service_page_redirect_if_not_logged_in(self):
        response = self.client.get('/service/create/1')
        self.assertRedirects(response, '/accounts/login/?next=/service/create/1')

    def test_edit_experience_page_redirect_if_not_logged_in(self):
        response = self.client.get('/experience/create/1')
        self.assertRedirects(response, '/accounts/login/?next=/experience/create/1')

    def test_edit_case_page_redirect_if_not_logged_in(self):
        response = self.client.get('/case/create/1')
        self.assertRedirects(response, '/accounts/login/?next=/case/create/1')


    def test_logged_in_uses_correct_template(self):
        c = Client()
        response = c.post('/login/', {'username': 'monusri', 'password': 'hellyeah@2019'})
        self.assertEqual(response.status_code, 200)
        
