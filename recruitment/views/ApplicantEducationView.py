# from django.views import View
# from django.views.generic import TemplateView, View, ListView
# from django.views.generic.base import  View
# from django.views.generic.edit  import CreateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .__init__ import *
from aeams.models import TblDomains as Domains, TblApplicantEducations as ApplicantsEducations
import json

# from django.shortcuts import render
# from recruitment.models import Applicants
# from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
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

def saveEducation(applicant_educations, applicant_id, appExp, creater):

    if (ApplicantsEducations.objects.filter(applicant_id=applicant_id)):
        ApplicantsEducations.objects.filter(applicant_id=applicant_id).delete()

    for ae in applicant_educations:
        # print(ax)
        if (not ae['education_id'] or not ae['institute_id'] or not ae['major_id']):
            pass
        else:
            # print(ae['education_id'])
            # print(ae['major_id'])
            # print(ae['institute_id'])
            education_id = Domains.objects.filter(id=ae['education_id']).first()
            major_id = Domains.objects.filter(id=ae['major_id']).first()
            institute_id = Domains.objects.filter(id=ae['institute_id']).first()

            if (not ae['institute']):
                inst = ''
            else:
                inst = ae['institute'];

            aeObj = ApplicantsEducations(applicant=appExp,
                                         education=education_id,
                                         major=major_id,
                                         year=ae['year'],
                                         institute=institute_id,
                                         institut=inst,
                                         created_by=creater,
                                         created=datetime.datetime.now())
            # aeObj = ApplicantsEducations(employee_id=var_applcant.id,
            #                           education_id=Domains.objects.get(id=ae['education_id']),
            #                           major_id=Domains.objects.get(id=ae['major_id']),
            #                           year=ae['year'],
            #                           institute_id=Domains.objects.get(id=ae['institute_id']),
            #                           institut=ae['institute'],
            #                           created=datetime.datetime.now())
            # aeObj = ApplicantsEducations(employee_id=var_applcant.id,
            #                              education_id=ae['education_id'],
            #                              major_id=ae['major_id'],
            #                              year=ae['year'],
            #                              institute_id=ae['institute_id'],
            #                              institut=ae['institute'],
            #                              created=datetime.datetime.now())
            aeObj.save()

    return True