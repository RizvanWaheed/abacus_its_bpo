# from django.views import View
# from django.views.generic import TemplateView, View, ListView
# from django.views.generic.base import  View
# from django.views.generic.edit  import CreateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q
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

def searchApplicantCnic(request): #, **self. _kwargs):
    # print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        # cnic = request.POST.get('cnicNumber', None)
        # print(cnic)
        applicant = Applicants.objects.filter(cnic=data['cnicNumber']).values()
        # print(applicant)
        # applicant_list = {'applicant': list(applicant)[0]}
        applicant_list = list(applicant)
        # print(applicant_list['applicant'])
        # print(applicant_list['applicant'].get('id'))
        # applicant_list = serializers.serialize('json', applicant)
        # print(applicant_list)
        if (not applicant_list):
            # var = Maincontrol.objects.filter(pageaccess_id=1, create=1)
            # if (not var):
            #     return JsonResponse({'error': 'Applicant not Found'})
            # else:
            return JsonResponse({'errorr': 'Applicant not Found', 'success_status': False}, status=201)
        else:
            # data = {'item': x.item, 'device': x.device, 'log': x.log}
            # applicant_list[0].append({'applicant_educations': list(ApplicantsEducations.objects.filter(applicant_id=applicant_list[0].get('id'))) })
            # appli_list[] = applicant_list[0]
            applicant_educations = ApplicantsEducations.objects.filter(
                applicant_id=applicant_list[0].get('id')).values();
            # print(list(applicant_educations))
            applicant_orientations = ApplicantOrientation.objects.filter(applicant_id=applicant_list[0].get('id'), active=1).values();
            applicant_list[0]['applicant_orientations'] = list(applicant_orientations)
            applicant_list[0]['applicant_educations'] = list(applicant_educations)

            applicant_list[0]['applicant_experiences'] = list(
                ApplicantsExperiences.objects.filter(applicant_id=applicant_list[0].get('id')).values())
            applicant_list[0]['applicant_refers'] = list(
                ApplicantsRefers.objects.filter(applicant_id=applicant_list[0].get('id')).values())
            applicant_list[0]['applicant_comments'] = list(ApplicantsComments.objects.filter(
                applicant_id=applicant_list[0].get(
                    'id')).values())  # 'created','remarks','created_by_id__username','created_by_id'))

            return JsonResponse({'applicant': applicant_list[0], 'success_status': True}, safe=False)

    return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)

def searchTodayApplicantList(request):
    print(request.GET)
    # print(request.body)
    # print(request.POST)
    # data = json.loads(request.body)

    fm_date = datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
    to_date = datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')

    state = request.GET.get('state', None)
    # print(cnic)
    applicant = Applicants.objects.filter(state_name=state).values()
    print(applicant)
    # applicant_list = {'applicant': list(applicant)[0]}
    applicant_list = list(applicant)
    # print(applicant_list['applicant'])
    # print(applicant_list['applicant'].get('id'))
    # applicant_list = serializers.serialize('json', applicant)
    print(applicant_list)
    return JsonResponse({'applicant': applicant_list, 'success_status': True}, safe=False)
    # return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)

def searchAllApplicantList(request):
    print(request.GET)
    # print(request.body)
    # print(request.POST)
    # data = json.loads(request.body)

    state = request.GET.get('state', None)
    # print(cnic)
    applicant = Applicants.objects.filter(state=state).values()
    print(applicant)
    # applicant_list = {'applicant': list(applicant)[0]}
    applicant_list = list(applicant)
    # print(applicant_list['applicant'])
    # print(applicant_list['applicant'].get('id'))
    # applicant_list = serializers.serialize('json', applicant)
    print(applicant_list)
    return JsonResponse({'applicant': applicant_list, 'success_status': True}, safe=False)
    # return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)

def getApplicants(request):
    print(request.GET)
    sub_state_id = request.GET.get('status', None)
    # sub_state_id = request.GET.get('sub_state_id', None)
    project_id = request.GET.get('project_id', None)
    officer = request.GET.get('officer', None)
    approved_by = request.GET.get('approved_by', None)


    fromdate =  datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')+" 00:00:00"
    todate = datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')+" 23:59:59"
    # print(state_id)
    # print(fromdate) #.strftime('%Y-%m-%d')+"T00:00:00")
    # print(todate) #.strftime('%Y-%m-%dT%H:%M:%S'))
    # applicant = Applicants.objects.filter(state=state,modified__gte=fromdate, modified__lte=todate).values()

    fc = Q(modified__gte=fromdate, modified__lte=todate)

    # state_is_none = Q(state__isnull=True)
    # state_is_not_none = Q(state=state)
    # applicant = Applicants.objects.filter(fc & ( state_is_none | state_is_not_none ) ).values()

    if sub_state_id:
        fc &= Q(sub_state_id=sub_state_id)
    if project_id:
        fc &= Q(project_id=project_id)
    if officer:
        fc &= Q(selected_by_id=officer)

    applicant = Applicants.objects.filter(fc).values('first_name', 'last_name', 'project__name', 'selected_by__name','id','state_name','contact', 'selected')

    # print(applicant.query)
    #
    # print(applicant)
    # applicant_list = {'applicant': list(applicant)[0]}
    applicant_list = list(applicant)
    # print(applicant_list['applicant'])
    # print(applicant_list['applicant'].get('id'))
    # applicant_list = serializers.serialize('json', applicant)
    # print(applicant_list)
    return JsonResponse({'applicant': applicant_list, 'success_status': True}, safe=False)


def downloadRecruitmentReport(request):
    # Create the HttpResponse object with the appropriate CSV header.
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.



    print(request.GET)
    # print(request.body)
    # print(request.POST)
    # data = json.loads(request.body)

    state = request.GET.get('state', None)
    # print(cnic)
    applicant = Applicants.objects.filter(state=state).values()
    print(applicant)
    # applicant_list = {'applicant': list(applicant)[0]}
    applicant_list = list(applicant)
    # print(applicant_list['applicant'])
    # print(applicant_list['applicant'].get('id'))
    # applicant_list = serializers.serialize('json', applicant)
    print(applicant_list)
    return JsonResponse({'applicant': applicant_list, 'success_status': True}, safe=False)
    # return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)



def setScheduler(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(request.user.id);


        print(data['applicant_id'])
        print(data['schedule_on'])
        print(data['schedule_with'])
        # var_applcant = Applicants.objects.get_or_create(cnic=data['cnic'])
        # print(request.body)
        # print(request.META.get('CONTENT-TYPE'))
        # del data['cnic']
        retr = {'message': 'Saved Successfully', 'success_status': True}
        code = 200
        try:
            creater = Users.objects.filter(id=request.user.id).first()
            if (not data['applicant_id'] or not data['schedule_on'] or not data['schedule_with']):
                retr = {'message': 'Data is not complete', 'success_status': False}
                code = 204
                pass
            else:
                if (ApplicantSchedulers.objects.filter(applicant_id=data['applicant_id'])):
                    ApplicantSchedulers.objects.filter(applicant_id=data['applicant_id']).update(status=0,modified_by=creater)


                scheduled = Users.objects.filter(id=data['schedule_with']).first()
                applicant = Applicants.objects.filter(id=data['applicant_id']).first()
                axObj = ApplicantSchedulers(applicant=applicant,
                                            schedule_on=data['schedule_on'],
                                            schedule_with= scheduled,
                                            status=1,
                                            created_by=creater)
                    # print(axObj)
                axObj.save()

        except SuspiciousOperation:
            retr = {'message': 'Failed To Save! Try again', 'success_status': False}
            code = 204
            pass
        return JsonResponse(retr, status=code)
    return JsonResponse({'message': 'Wrong Request ', 'success_status': False}, status=404)