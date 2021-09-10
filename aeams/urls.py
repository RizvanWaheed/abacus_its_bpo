from django.urls import path
from django.conf.urls import url, include
from aeams.views.authentication import login, logout
from aeams.views import dashboard

from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
# from . views import home
# from . views import home
# from . views import walkIn, fromHome, tplApplicant, searchApplicant, saveApplicant


urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    # path('set_basic_options', domains.set_basic_options, name='set_basic_options'),
    # path('dashboard', dashboard.index, name='dashboard'),
    path('<str:page>', dashboard.index, name='index'),

    #   path('recruitments/<str:page>', dashboard.recruitments, name='recruitments'),
    #   path('', walkIn, name='walk_in'),
    #   path('from_home', fromHome, name='from_home'),
    #   path('search_applicant', searchApplicant, name='search_applicant'),
    #   path('save_applicant', saveApplicant, name='save_applicant'),
]
