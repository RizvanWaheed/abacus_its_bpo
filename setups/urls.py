from django.urls import path
from setups.views import DomainsView as domains, SetupsView as setup

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
# from . views import home
# from . views import home
# from . views import walkIn, fromHome, tplApplicant, searchApplicant, saveApplicant


urlpatterns = [
    path('set_basic_options', domains.set_basic_options, name='set_basic_options'),
    path('<str:page>', setup.index, name='index'),
    # path('dashboard', dashboard.index, name='dashboard'),


    #   path('recruitments/<str:page>', dashboard.recruitments, name='recruitments'),
    #   path('', walkIn, name='walk_in'),
    #   path('from_home', fromHome, name='from_home'),
    #   path('search_applicant', searchApplicant, name='search_applicant'),
    #   path('save_applicant', saveApplicant, name='save_applicant'),
]
