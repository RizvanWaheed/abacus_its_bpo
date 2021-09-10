from django.urls import path
from .views import ApplicantOrientationView, ApplicantsScoreView
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView

# from . views import home
# from aeams.views import authentication
# from . views import home
# from . views import walkIn, fromHome, tplApplicant, searchApplicant, saveApplicant
#

urlpatterns = [

    path('search_applicant', login_required(ApplicantsScoreView.searchApplicantCnic), name="search_applicant"),
    # path('search_today_applicant', login_required(ApplicantsView.searchTodayApplicantList), name="search_today_applicant"),
    # path('search_applicant_assesment', login_required(ApplicantsView.searchAllApplicantList), name="search_applicant_assesment"),
    # path('download_applicant_assesment', login_required(ApplicantsView.downloadRecruitmentReport), name="download_applicant_assesment"),
    # path('applicant_assesment', login_required(ApplicantsView.setApplicantAssesment), name="applicant_assesment"),
    # path('applicant_selected', login_required(ApplicantsView.getApplicants), name="applicant_selected"),
    # path('set_scheduler', login_required(ApplicantSchedulerView.setScheduler), name="set_scheduler"),

    path('set_orientation', login_required(ApplicantOrientationView.setOrientation), name="set_orientation"),
    path('applicant_score', login_required(ApplicantsScoreView.getApplicantOrientationScore), name="applicant_score"),
    path('get_orientation', login_required(ApplicantOrientationView.getOrientation), name="get_orientation"),

    path('<str:page>', ApplicantsScoreView.index, name='index'),

    #   path('applications/', )
    #   for complete view calling get and post function
    #   path('applicants/', ApplicantsView.ApplicantsView.as_view()), #name="search_applicant"),
    #   path('logout', authentication.logout, name='logout'),
    #   path('index', home.index , name='index'),
    #   path('', walkIn, name='walk_in'),
    #   path('from_home', fromHome, name='from_home'),
    #   path('search_applicant', searchApplicant, name='search_applicant'),
    #   path('save_applicant', saveApplicant, name='save_applicant'),

]

