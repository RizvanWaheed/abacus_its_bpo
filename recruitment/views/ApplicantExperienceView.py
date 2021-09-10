# from django.views import View
# from django.views.generic import TemplateView, View, ListView
# from django.views.generic.base import  View
# from django.views.generic.edit  import CreateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .__init__ import *
from aeams.models import TblApplicantExperiences as ApplicantsExperiences
import json
from django.core.exceptions import SuspiciousOperation
# from django.shortcuts import render
# from recruitment.models import Applicants
# from django.http import JsonResponse
# from django.core import serializers
# from django.views.decorators import csrf_exempt
# Create your views here.

#class ApplicantsView(View):

    # geatings = "found in List"
    #
    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


def saveExperiences(applicant_experiences, applicant_id, appExp, creater):

    if (ApplicantsExperiences.objects.filter(applicant_id=applicant_id)):
        ApplicantsExperiences.objects.filter(applicant_id=applicant_id).delete()

    for ax in applicant_experiences:
        # print(ax)
        if (not ax['company_name'] or not ax['designation'] or not ax['started'] or not ax['ended']):
            pass
        else:
            axObj = ApplicantsExperiences(applicant=appExp,
                                          company_name=ax['company_name'],
                                          designation=ax['designation'],
                                          started=ax['started'],
                                          ended=ax['ended'],
                                          job_description=ax['job_description'],
                                          created_by=creater)

            axObj.save()

    return True