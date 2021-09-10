# from django.views import View
# from django.views.generic import TemplateView, View, ListView
# from django.views.generic.base import  View
# from django.views.generic.edit  import CreateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q, F
from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .__init__ import *
from aeams.models import ApplicantSchedulers, TblUsers as Users, TblDomains as Domains, TblSetups as Setups
from aeams.models import TblApplicant as Applicants, TblApplicantEducations as ApplicantsEducations, TblApplicantOrientations as ApplicantOrientation
from aeams.models import TblApplicantExperiences as ApplicantsExperiences, TblApplicantRefers as ApplicantsRefers, TblApplicantComments as ApplicantsComments
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

def setOrientation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(request.user.id);
        # var_applcant = Applicants.objects.get(cnic=data['cnic'])


        # var_applcant = Applicants.objects.get_or_create(cnic=data['cnic'])
        # print(request.body)
        # print(request.META.get('CONTENT-TYPE'))
        # del data['cnic']
        retr = {'message': 'Saved Successfully', 'success_status': True}
        code = 200
        try:
            creater = Users.objects.filter(id=request.user.id).first()
            applicant_orientations = data['applicant_orientations']

            appExp = Applicants.objects.filter(id=data['id']).first()

            if data['typing'] == 'manger':
                data['typing'] = 'op_manager'
            elif data['typing'] == 'lead':
                data['typing'] = 'op_lead'
            # else:
            #     data['typing'] = 'Fraud'

            if (ApplicantOrientation.objects.filter(applicant_id=data['id'], role=data['typing'])):
                ApplicantOrientation.objects.filter(applicant_id=data['id']).update(status=F('status')+1,active=0, modified_by=creater)

            elif (ApplicantOrientation.objects.filter(applicant_id=data['id'])):
                ApplicantOrientation.objects.filter(applicant_id=data['id']).update(active=0, modified_by=creater)
                # ExistingApplicantOrientation = ApplicantOrientation.objects.get(applicant_id=data['id'])
                # ExistingApplicantOrientation.active = 0
                # ExistingApplicantOrientation.save()

            for ao in applicant_orientations:
                for aoc in ao['children']:
                    # print(ao)
                    # print(aoc['id'])
                    # print(aoc['status'])
                    # print(aoc['group'])
                    # if (aoc['status'] == 0):
                    #     pass
                    # else:
                    orientation_id = Setups.objects.filter(id=aoc['id']).first()

                    aocObj = ApplicantOrientation(applicant=appExp,
                                                  orientation=orientation_id,
                                                  orientation_level=aoc['group'],
                                                  active=1,
                                                  status=1,
                                                  created_by=creater,
                                                  role=data['typing'],
                                                  checked=aoc['status'],
                                                  created=datetime.datetime.now())
                    aocObj.save()

        except SuspiciousOperation:
            retr = {'message': 'Failed To Save! Try again', 'success_status': False}
            code = 204
            pass
        return JsonResponse(retr, status=code)
    return JsonResponse({'message': 'Wrong Request ', 'success_status': False}, status=404)


def getOrientation(request):

    # fm_date = request.GET.get('from', None)
    # to_date = request.GET.get('to', None)
    # sub_state_id = request.GET.get('sub_state_id', None)
    typing = request.GET.get('typing', None)
    print(typing)
    fc = Q(base_id=2500, status=1)
    if typing == 'manager' or typing == 'lead':
        fc &= Q(slug__contains='_op_')
    if typing == 'trainer':
        fc &= Q(slug__contains='_trainer_')

    # applicant = Applicants.objects.filter(fc).values()
    # applicant = Applicants.objects.filter(fc).values().prefetch_related('ApplicantOrientation_set').values()
    # .prefetch_related('ApplicantOrientation_set').values()

    orientationObj = Setups.objects.filter(fc).values('id', 'name', 'group', 'slug', 'parent_id',
                                                                          'status')
    print(orientationObj.query)
    orientation_list = list(orientationObj)
    return JsonResponse({'orientations': orientation_list, 'success_status': True}, safe=False)
    # applicant = Applicants.objects.filter(fc).values('id', 'full_name', 'project__name', 'joining_date')
    # applicant_list = list(applicant)
    # print(applicant)
    # print(applicant_list)

