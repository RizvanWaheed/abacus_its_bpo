from django.urls import path
from . views import walkIn, fromHome, tplApplicant, searchApplicant, saveApplicant

# from . views import recruitment_view
# from . views import authentication
# from . views import signup
# from . views import home
# from .	views import report
# from . views import ajax
# from . views import main
# from . views import assign_role_to_users
# from . views import addemp_view
urlpatterns = [
    path('', walkIn, name='walk_in'),
    path('from_home', fromHome, name='from_home'),
    path('search_applicant', searchApplicant, name='search_applicant'),
    path('save_applicant', saveApplicant, name='save_applicant'),
    path('tpl_applicant', tplApplicant, name='tpl_applicant'),
 ]
