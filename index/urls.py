from django.conf import settings
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views
from .forms import UserLoginForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('details/<int:id>', views.details, name="details"),
    path('search', views.search, name="search"),

]

# Add URLConf to create, update, and delete orgs
urlpatterns += [
    path('register', views.OrgbaseInfoCreate.as_view(), name="register"),
    path('editPage/<int:pk>', views.OrgBaseInfoUpdate.as_view(), name="editPage"),
    path('delete/<int:pk>', views.OrgDelete, name="org_delete"),
]

# Add URLConf to create, update, and delete Industry
urlpatterns += [
    path('editIndustry', views.EditIndustryOptions, name="options_industry"),
]

# Add URLConf to create, update, and delete experiences
urlpatterns += [
    path('experience/create/<int:pk>',
         views.ExperienceCreate.as_view(), name='experience_create'),
    path('experience/update/<int:pk>/',
         views.ExperienceUpdate.as_view(), name='experience_update'),
    path('experience/delete/<int:id>/',
         views.ExperienceDelete, name='experience_delete')
]
# Add URLConf to create, update, and delete Services
urlpatterns += [
    path('service/create/<int:pk>',
         views.ServiceCreate.as_view(), name='service_create'),
    path('service/update/<int:pk>/',
         views.ServiceUpdate.as_view(), name='service_update'),
    path('service/delete/<int:pk>/', views.ServiceDelete, name='service_delete')
]
# Add URLConf to create, update, and delete Cases
urlpatterns += [
    path('case/create/<int:pk>', views.CaseCreate.as_view(), name='case_create'),
    path('case/update/<int:pk>/', views.CaseUpdate.as_view(), name='case_update'),
    path('case/delete/<int:pk>/', views.CaseDelete, name='case_delete')
]

# amend AuthenticationForm
urlpatterns += [
    path('login/', LoginView.as_view(template_name="registration/login.html",
                                     authentication_form=UserLoginForm), name='login'),
]

# Serving Staticfile during development
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
