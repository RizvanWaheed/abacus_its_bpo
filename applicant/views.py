from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
import datetime
from .__init__ import *
from aeams.models import TblUsers as Users, TblDomains as Domains
from aeams.models import TblApplicant as Applicants, TblApplicantEducations as ApplicantsEducations
from aeams.models import TblApplicantExperiences as ApplicantsExperiences, TblApplicantRefers as ApplicantsRefers, TblApplicantComments as ApplicantsComments
# from django.shortcuts import render
# from recruitment.models import Applicants
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import SuspiciousOperation
from django.core import serializers
# from django.views.decorators import csrf_exempt
# Create your views here.

def walkIn(request):
    citiesObj = Domains.objects.filter(domain_type='City', status=1 ).values('id', 'name')
    # citiesData = serializers.serialize('json', [citiesObj, ])
    # print(citiesData)
    languagesObj = Domains.objects.filter(domain_type='Language', status=1).values('id', 'name')
    # languagesData = serializers.serialize('json', [languagesObj, ])
    educationsObj = Domains.objects.filter(domain_type='Education', status=1).values('id', 'name')
    # educationsData = serializers.serialize('json', [educationsObj, ])
    institutesObj = Domains.objects.filter(domain_type='Institutes', status=1).values('id', 'name')
    # institutesData = serializers.serialize('json', [institutesObj, ])
    majorsObj = Domains.objects.filter(domain_type='Majors', status=1).values('id', 'name')
    # majorsData = serializers.serialize('json', [majorsObj, ])

    return render(request, 'applicant/index.html',
                  context={'variable': 'Walk In', 'currDate': datetime.datetime.now(),
                           'cities': list(citiesObj),
                           'educations': list(educationsObj),
                           'institutes': list(institutesObj),
                           'languages': list(languagesObj),
                           'majors': list(majorsObj)})

    # return render(request, 'applicant/index.html',
    #               context = {'variable': 'Walk In', 'currDate': datetime.datetime.now(), 'cities': json.dumps(citiesObj),
    #                'languages': json.dumps(languagesObj), 'educations': json.dumps(educationsObj), 'institutes': json.dumps(institutesObj),
    #                'majors': json.dumps(majorsObj)})
    # return render(request,'applicant/index.html', {'variable': 'Walk In', 'currDate':datetime.datetime.now(),'cities':citiesData,'languages':languagesData,'educations':educationsData,'institutes':institutesData,'majors':majorsData})

def fromHome(request):
    return render(request,'applicant/index.html', {'variable': 'From Home'})

def tplApplicant(request):
    return render(None,'applicant/tpl_applicants.html')

@csrf_exempt
def searchApplicant(request):
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
        #applicant_list = serializers.serialize('json', applicant)
        print(applicant_list)
        if (not applicant_list):
            # var = Maincontrol.objects.filter(pageaccess_id=1, create=1)
            # if (not var):
            #     return JsonResponse({'error': 'Applicant not Found'})
            # else:
            return JsonResponse({'errorr': 'Applicant not Found', 'success_status': False }, status=201)
        else:
            # data = {'item': x.item, 'device': x.device, 'log': x.log}
            # applicant_list[0].append({'applicant_educations': list(ApplicantsEducations.objects.filter(applicant_id=applicant_list[0].get('id'))) })
            # appli_list[] = applicant_list[0]
            applicant_educations = ApplicantsEducations.objects.filter(applicant_id=applicant_list[0].get('id')).values();
            print(list(applicant_educations))
            applicant_list[0]['applicant_educations'] = list(applicant_educations)

            applicant_list[0]['applicant_experiences'] = list(ApplicantsExperiences.objects.filter(applicant_id=applicant_list[0].get('id')).values())
            applicant_list[0]['applicant_refers'] =  list(ApplicantsRefers.objects.filter(applicant_id=applicant_list[0].get('id')).values())
            applicant_list[0]['applicant_comments'] = list(ApplicantsComments.objects.filter(applicant_id=applicant_list[0].get('id')).values())#'created','remarks','created_by_id__username','created_by_id'))

            return JsonResponse({'applicant': applicant_list[0], 'success_status': True }, safe=False)

    return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)

@csrf_exempt
def saveApplicant(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        creater = Users.objects.filter(id=1).first()
        ipaddress = request.META.get("REMOTE_ADDR");
        # re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ipaddress)

        # ipaddress = "10.128.215.10"

        centerid = 11
        if "192.168.101" in ipaddress:
            centerid = 498
        elif "10.128.216" in ipaddress:
            centerid = 498
        elif "10.128.215" in ipaddress:
            centerid = 498
        elif "10.128.212" in ipaddress:
            centerid = 498
        elif "10.128.211" in ipaddress:
            centerid = 498
        elif "10.128.210" in ipaddress:
            centerid = 498
        elif "192.168.102" in ipaddress:
            centerid = 499
        elif "10.128.217" in ipaddress:
            centerid = 499
        elif "10.128.218" in ipaddress:
            centerid = 499


        # if ipaddress.find("192.168.101") != -1 or ipaddress.find("10.128.216") != -1 or ipaddress.find(
        #         "10.128.215") != -1 or ipaddress.find("10.128.211") != -1 or ipaddress.find("10.128.210"):
        #
        #     print
        #     "Found Lahore!"
        #
        # elif ipaddress.find("192.168.102") != -1 or ipaddress.find("10.128.217") != -1 or ipaddress.find(
        #         "10.128.218") != -1:
        #     centerid = 399
        #     print
        #     "Found Islamabad!"

        # print(data['cnic'])
        # var_applcant = Applicants.objects.get_or_create(cnic=data['cnic'])
        # print(request.body)
        # print(request.META.get('CONTENT-TYPE'))
        # del data['cnic']


        retr = {'message': 'Saved Successfully', 'success_status': True}
        code = 200
        try:
            if (Applicants.objects.filter(cnic=data['cnic'])):
                var_applcant = Applicants.objects.get(cnic=data['cnic'])
            else:
                var_applcant = Applicants()

            var_applcant.cnic = data['cnic']
            var_applcant.cnic_insurance_date = data['cnic_insurance_date'] # datetime.datetime.strptime(data['cnic_insurance_date'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
            var_applcant.first_name = data['first_name']

            if data['last_name'] == '':
                var_applcant.last_name = data['last_name']
            else:
                var_applcant.last_name = ""

            var_applcant.father_name = data['father_name']
            var_applcant.gender = data['gender']
            var_applcant.dob = data['dob'] # datetime.datetime.strptime(data['dob'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')

            # var_applcant.marital_status = data['marital_status']
            if data['marital_status'] == '':
                var_applcant.marital_status = 'Single'
            else:
                var_applcant.marital_status = data['marital_status']

            var_applcant.contact = data['contact']

            if data['eaddress'] == '':
                var_applcant.eaddress = 'xyz@rizvan.com'
            else:
                var_applcant.eaddress = data['eaddress']

            var_applcant.city_id = data['city_id']

            # var_applcant.language_id = data['language_id']


            var_applcant.address = data['address']
            var_applcant.state_name = data['state']
            var_applcant.source = data['source']

            var_applcant.ip_address = ipaddress
            var_applcant.center_id = centerid


            # var_applcant.ApplicantsEducations =
            # var_applcant.department_id = data['department']
            # var_applcant.designation_id = data['desigination']
            # var_applcant.project_id = data['project']
            var_applcant.created_by = creater
            var_applcant.created = datetime.datetime.now()
            var_applcant.state_id = 287
            var_applcant.sub_state_id = 287
            #print('before save')

            var_applcant.save()
            appExp = Applicants.objects.filter(id=var_applcant.id).first()

            comments = data['comments'];
            acObj = ApplicantsComments(applicant=appExp,
                                       remarks=comments,
                                       status=1,
                                       state_id=287,
                                       sub_state_id=287,
                                       created_by=creater)
            print(acObj)
            acObj.save()

            applicant_educations = data['applicant_educations']
            if (ApplicantsEducations.objects.filter(applicant_id=var_applcant.id)):
                ApplicantsEducations.objects.filter(applicant_id=var_applcant.id).delete()
            for ae in applicant_educations:
                # print(ae)
                if (not ae['education_id'] or not ae['institute_id'] or not ae['major_id']):
                    pass
                else:
                    # print(ae['education_id'])
                    # print(ae['major_id'])
                    # print(ae['institute_id'])
                    education_id = Domains.objects.filter(id=ae['education_id']).first()
                    major_id = Domains.objects.filter(id=ae['major_id']).first()
                    institute_id =Domains.objects.filter(id=ae['institute_id']).first()
                    aeObj = ApplicantsEducations(applicant=appExp,
                                                 education=education_id,
                                                 major=major_id,
                                                 year=ae['year'],
                                                 institute=institute_id,
                                                 institut=ae['institute'],
                                                 created_by = creater,
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

            applicant_experiences = data['applicant_experiences']

            if (ApplicantsExperiences.objects.filter(applicant_id=var_applcant.id)):
                ApplicantsExperiences.objects.filter(applicant_id=var_applcant.id).delete()

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
                                              created_by = creater)
                # print(axObj)
                axObj.save()
                # started = datetime.datetime.strptime(ax['started'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d'),
                # ended = datetime.datetime.strptime(ax['ended'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d'),

            applicant_refers = data['applicant_refers']

            for ar in applicant_refers:
                # print(ar)
                education_id = Domains.objects.filter(id=ar['education_id']).first()
                arObj = ApplicantsRefers(applicant=appExp,
                                              phone=ar['phone'],
                                              name=ar['name'],
                                              education=education_id,
                                              created_by=creater)
                # print(arObj)

                arObj.save()

        except SuspiciousOperation:
            retr = {'message': 'Failed To Save! Try again', 'success_status': False}
            code = 204
            pass
        return JsonResponse(retr, status=code)
    return JsonResponse({'message': 'Wrong Request ', 'success_status': False }, status=404)
