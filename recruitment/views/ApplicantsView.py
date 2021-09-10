# from django.views import View
# from django.views.generic import TemplateView, View, ListView
# from django.views.generic.base import  View
# from django.views.generic.edit  import CreateView
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Q, F
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from .__init__ import *
from aeams.models import TblEmployees as Employees
from aeams.models import TblUsers as Users, TblDomains as Domains, TblSetups as Setups, ApplicantSchedulers, \
    TblSetupSetups as setupSetups
from aeams.models import TblApplicant as Applicants, TblApplicantEducations as ApplicantsEducations, \
    TblApplicantOrientations as ApplicantOrientation
from aeams.models import TblApplicantExperiences as ApplicantsExperiences, TblApplicantRefers as ApplicantsRefers, \
    TblApplicantComments as ApplicantsComments
import json
# for csv start
import csv
from django.http import StreamingHttpResponse
# for csv end

# from django.shortcuts import renderz
# from recruitment.models import Applicants
# from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
# from django.core import serializers
# from django.views.decorators import csrf_exempt
# Create your views here.
from django.db import connection, OperationalError

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


# class ApplicantsView(View):

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
def index(request, page=None, access=None, permission=None, aptype=None):
    # print(request)
    # print(request)
    # print('page')
    # print(page)
    # print('page')
    if request.session.has_key('is_logged'):
        # print(self.request.user)
        # print(request.user.role_id)
        accessObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='recruitment', active=1).values(
            'type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug',
            'sub_setup__group', 'sub_setup__id')
        # 'setup_id', 'type', 'sub_setup__name', 'sub_setup__slug', 'sub_setup__group', 'sub_setup__id', 'sub_setup__base_id'
        # print(accessObj)
        if (not accessObj):
            return redirect('/aeams/logout')
        accessObjTree = []
        for aO in accessObj:
            parent = {}
            if (aO['sub_setup__parent_id'] == aO['sub_setup__base_id']):
                parent = aO
                children = []
                for aOl2 in accessObj:
                    if (aOl2['sub_setup__parent_id'] == aO['sub_setup__id']):
                        children.append(aOl2)
                    else:
                        pass

                parent['children'] = children
            else:
                pass

            if (bool(parent)):
                accessObjTree.append(parent)

        print(accessObjTree)
        # 	accessObjTree.append(aO)
        # 	aO['children'] = {}
        # 	accessObjTree[aO['sub_setup__parent_id']] = aO
        # else:
        # 	if(not accessObjTree[aO['sub_setup__parent_id']]['children']):
        # 		accessObjTree[aO['sub_setup__parent_id']]['children'] = {}
        # 	accessObjTree[aO['sub_setup__parent_id']]['children'] = aO
        # print(accessObjTree)
        # print(request.user.role_id)
        # print(request.user)
        # index_page = 'aeams/'
        # if page == 'applicant_score' or page == 'new_assesment':
        # 	index_page += 'index_assesment.html'
        # if page == 'recruitment' or page == 'recruitment_report' or page == 'interview_call' or page == 'interview_approval':
        # 	index_page += 'index_angularjs.html'

        officerObj = Users.objects.filter(role__slug__contains='_RO_', status=1).values('id', 'name')
        managerObj = Users.objects.filter(role__slug__contains='_RM_', status=1).values('id', 'name')
        headObj = Users.objects.filter(role__slug__contains='_RH_', status=1).values('id', 'name')

        traineeObj = Users.objects.filter(role__slug__contains='_AT_', status=1).values('id', 'name')
        leadObj = Users.objects.filter(role__slug__contains='_AL_', status=1).values('id', 'name')

        # lambda Expression With substring
        # stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1).values('id', 'name', 'group', 'slug', 'parent_id', 'status')
        # print(officerObj)
        # print(filter(lambda x: x.id == request.user.id, officerObj))
        iam_ro = list(filter(lambda x: x['id'] == request.user.id, officerObj))
        iam_rm = list(filter(lambda x: x['id'] == request.user.id, managerObj))
        iam_rh = list(filter(lambda x: x['id'] == request.user.id, headObj))
        iam_at = list(filter(lambda x: x['id'] == request.user.id, traineeObj))
        iam_al = list(filter(lambda x: x['id'] == request.user.id, leadObj))
        # iamin =  list(map(lambda x: x['id'] == request.user.id, officerObj)) return [false, false]
        # print(iam)
        # print(iamin)
        # print(iam.get('id'))

        if (iam_ro):
            iam = 'officer'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')
        elif (iam_rm):
            iam = 'manager'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RM_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')
        elif (iam_rh):
            iam = 'head'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RH_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')
        elif (iam_at):
            iam = 'trainer'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_AT_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')
        elif (iam_al):
            iam = 'lead'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_AL_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')
        else:
            iam = 'None'
            stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id',
                                                                                                               'name',
                                                                                                               'group',
                                                                                                               'slug',
                                                                                                               'parent_id',
                                                                                                               'status')

        allStateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1).values('id', 'name',
                                                                                       'group',
                                                                                       'slug',
                                                                                       'parent_id',
                                                                                       'status')
        print(iam)
        print(headObj)

        departmentObj = Setups.objects.filter(base_id=2, status=1).values('id', 'name')
        designationObj = Setups.objects.filter(base_id=3, status=1).values('id', 'name')
        projectObj = Setups.objects.filter(base_id=1000, status=1, group='Projects').values('id', 'name')
        # if
        # 	_recruiter_
        orientationObj = Setups.objects.filter(base_id=2500, status=1, slug__contains='_recruiter_').values('id',
                                                                                                            'name',
                                                                                                            'group',
                                                                                                            'slug',
                                                                                                            'parent_id',
                                                                                                            'status')

        # religionObj = Domains.objects.filter(domain_type='Religion', status=1).values('id', 'name')
        # sectObj = Domains.objects.filter(domain_type='Sect', status=1).values('id', 'name')

        citiesObj = Domains.objects.filter(domain_type='City', status=1).values('id', 'name')
        # citiesData = serializers.serialize('json', [citiesObj, ])
        countriesObj = Domains.objects.filter(domain_type='country', status=1).values('id', 'name')
        # countriesData = serializers.serialize('json', [countriesObj, ])
        # print(countriesData)
        languagesObj = Domains.objects.filter(domain_type='Language', status=1).values('id', 'name')
        # languagesData = serializers.serialize('json', [languagesObj, ])
        educationsObj = Domains.objects.filter(domain_type='Education', status=1).values('id', 'name')
        # educationsData = serializers.serialize('json', [educationsObj, ])
        religionsObj = Domains.objects.filter(domain_type='Religion', status=1).values('id', 'name')
        # institutesData = serializers.serialize('json', [institutesObj, ])

        sectsObj = Domains.objects.filter(domain_type='Sect', status=1).values('id', 'name')

        # educationsData = serializers.serialize('json', [educationsObj, ])
        institutesObj = Domains.objects.filter(domain_type='Institutes', status=1).values('id', 'name')
        # institutesData = serializers.serialize('json', [institutesObj, ])
        majorsObj = Domains.objects.filter(domain_type='Majors', status=1).values('id', 'name')

        # majorsData = serializers.serialize('json', [majorsObj, ])
        #
        return render(request, 'recruitment/index_angularjs.html',
                      context={'variable': 'Select_Reject',
                               'role': iam,
                               'allStates': list(allStateObj),
                               'currDate': datetime.datetime.now(),
                               'access': list(accessObjTree),
                               'officers': list(officerObj),
                               'heads': list(headObj),
                               'states': list(stateObj),
                               'orientations': list(orientationObj),
                               'departments': list(departmentObj),
                               'designations': list(designationObj),
                               'projects': list(projectObj),
                               'cities': list(citiesObj),
                               'countries': list(countriesObj),
                               'educations': list(educationsObj),
                               'religions': list(religionsObj),
                               'sects': list(sectsObj),
                               'institutes': list(institutesObj),
                               'languages': list(languagesObj),
                               'majors': list(majorsObj)})

        # ,{'main_access':Maincontrol.objects.filter(role_id_id=request.user.roles_id)})
    else:
        return redirect('login')

# def need_domain

def searchApplicantCnic(request):  # , **self. _kwargs):
    # print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        # cnic = request.POST.get('cnicNumber', None)
        # print(cnic)

        CnicNumber = '-'.join([data['cnicNumber'][:5], data['cnicNumber'][5:12], data['cnicNumber'][12:]])

        # print(CnicNumber)

        applicant = Applicants.objects.filter(cnic=data['cnicNumber']).values() # .latest('created') #.order_by('-id')..first() # #.latest() #.order_by('-id')[:1]

        # print(applicant.get())
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
            # print(list(applicant_educations))
            applicant_orientations = ApplicantOrientation.objects.filter(applicant_id=applicant_list[0].get('id'),
                                                                         active=1).values();
            applicant_list[0]['applicant_orientations'] = list(applicant_orientations)

            if (data['form'] != 'assesment'):

                employeeinfo = Employees.objects.filter(cnic = CnicNumber).values('batch_no', 'joining_date'
                                                                                  , 'last_working_date', 'center__name'
                                                                                  , 'designation__name', 'department__name'
                                                                                  , 'project__name', 'campaign__name'
                                                                                  , 'sub_campaign__name')#, 'state__name'
                # print(list(employeeinfo))

                applicant_educations = ApplicantsEducations.objects.filter(
                    applicant_id=applicant_list[0].get('id')).values();
                applicant_list[0]['applicant_educations'] = list(applicant_educations)

                applicant_list[0]['applicant_experiences'] = list(
                    ApplicantsExperiences.objects.filter(applicant_id=applicant_list[0].get('id')).values())
                applicant_list[0]['applicant_refers'] = list(
                    ApplicantsRefers.objects.filter(applicant_id=applicant_list[0].get('id')).values())

                applicant_list[0]['applicant_comments'] = list(ApplicantsComments.objects.filter(
                    applicant_id=applicant_list[0].get(
                        'id')).values())  # 'created','remarks','created_by_id__username','created_by_id'))


            return JsonResponse({'applicant': applicant_list[0], 'employee': list(employeeinfo), 'success_status': True}, safe=False)

    return JsonResponse({'message': 'Server not responding ', 'success_status': False}, status=404)


def searchTodayApplicantList(request):
    print(request.GET)
    # print(request.body)
    # print(request.POST)
    # data = json.loads(request.body)

    creater = Users.objects.filter(id=request.user.id).values('employee__center_id').last() #.latest('employee__center_id')
    # print(creater.query)
    center = creater['employee__center_id']
    # print(creater['employee__center_id'])
    fm_date = request.GET.get('from', None)
    # datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
    to_date = request.GET.get('to', None)
    # datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')

    state = request.GET.get('state', None)
    desi = request.GET.get('form', None)

    fc = Q(modified__gte=fm_date, modified__lte=to_date, state_name=state)

    if desi != 'officer':
        fc = Q(schedule_on=fm_date, schedule_with_id=request.user.id, status=1, applicant_id__state_name=state)
        # fc &= Q()
        # schedule_on__gte=fm_date, schedule_on__lte=to_date, applicant_id__state_name=state,
        applicant = ApplicantSchedulers.objects.filter(fc).values('id', 'applicant_id', 'applicant_id__cnic',
                                                                  'applicant_id__gender', 'applicant_id__first_name',
                                                                  'applicant_id__last_name', 'applicant_id__dob',
                                                                  'applicant_id__contact')
        # .annotate(cnic='applicant_id__cnic')
        print(applicant.query)
        # applicant = Applicants.objects.filter(state_name=state).values('sche')
    else:
        applicant = Applicants.objects.filter(modified__gte=fm_date, state_name=state, center_id=center ).values('id', 'cnic', 'gender',
                                                                                              'first_name', 'last_name',
                                                                                              'dob', 'contact')
        # print(cnic)

    print(applicant.query)
    applicant_list = list(applicant)
    # applicant = Applicants.objects.filter(state_name=state).values()
    # applicant_list = {'applicant': list(applicant)[0]}
    # print(applicant_list['applicant'])
    # print(applicant_list['applicant'].get('id'))
    # applicant_list = serializers.serialize('json', applicant)
    # User.objects.select_related('foo').filter(Q(foo__isnull=True) | Q(<other criteria here>))
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
    # print(request.GET)
    state = request.GET.get('state', None)
    sub_state_id = request.GET.get('sub_state_id', None)
    # sub_state_id = request.GET.get('status', None)
    # sub_state_id = request.GET.get('sub_state_id', None)
    project_id = request.GET.get('project_id', None)
    officer = request.GET.get('officer', None)
    approved_by = request.GET.get('approved_by', None)

    fromdate = datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime(
        '%Y-%m-%d') + " 00:00:00"
    todate = datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime(
        '%Y-%m-%d') + " 23:59:59"
    # print(state_id)
    # print(fromdate) #.strftime('%Y-%m-%d')+"T00:00:00")
    # print(todate) #.strftime('%Y-%m-%dT%H:%M:%S'))
    # applicant = Applicants.objects.filter(state=state,modified__gte=fromdate, modified__lte=todate).values()

    fc = Q(created__gte=fromdate, created__lte=todate)

    if officer:
        fc = Q(selected__gte=fromdate, selected__lte=todate, selected_by_id=officer)

    if sub_state_id:
        fc &= Q(sub_state_id=sub_state_id)
    if project_id:
        fc &= Q(project_id=project_id)

    # state_is_none = Q(state__isnull=True)
    # state_is_not_none = Q(state=state)
    # applicant = Applicants.objects.filter(fc & ( state_is_none | state_is_not_none ) ).values()

    print(fc)


    select_args = ['id', 'first_name', 'last_name', 'project__name', 'selected_by__name', 'id', 'state_name', 'contact',
                   'selected']

    if state == 'selected':
        select_args.append('finalized_by__name')
        select_args.append('finalized')
    elif state == 'hire':
        select_args.append('approved_by__name')
        select_args.append('approved')

    applicant = Applicants.objects.filter(fc).select_related().values(*tuple(select_args))
    print(applicant.query)
    applicant_list = list(applicant)
    # print(applicant_list)
    # print(applicant_list[0])
    # print(applicant_list[0].get('id'))
    # add date for greater then current date appointment.
    # else:
    #     applicant_list[0]['applicant_scheduler'] = list([{ "schedule_on": "None", "schedule_with__name": "None"}])

    if (applicant_list):
        for index, item in enumerate(applicant_list):
            print(item)
            applicant_scheduler = ApplicantSchedulers.objects.filter(applicant_id=item.get('id'),
                                                                     status=1).values('schedule_on',
                                                                                      'schedule_with__name');
            # print(list(applicant_scheduler))
            if (applicant_scheduler):
                applicant_list[index]['applicant_scheduler'] = list(applicant_scheduler)[0]

    return JsonResponse({'applicant': applicant_list, 'success_status': True}, safe=False)


def downloadApplicant(request):

    # Create the HttpResponse object with the appropriate CSV header.
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    # The data is hard-coded here, but you could load it from a database or
    # some other source.

    print(request.GET)
    # print(request.body)
    # print(request.POST)
    # data = json.loads(request.body)

    officer = request.GET.get('officer', None)
    approved_by = request.GET.get('approved_by', None)
    project_id = request.GET.get('project_id', None)
    # T%H:%M:%S.%f%z
    fm_date = datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%d').strftime(
        '%Y-%m-%d') + " 00:00:00"
    to_date = datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%d').strftime(
        '%Y-%m-%d') + " 23:59:59"

    # fm_date = request.GET.get('from', None)
     # datetime.datetime.strptime(request.GET.get('from', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
    # to_date = request.GET.get('to', None)
    # datetime.datetime.strptime(request.GET.get('to', None), '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
    state = request.GET.get('status', None)
    print(fm_date)
    print(to_date)
    print(officer)

    fc = Q(created__gte=fm_date, created__lte=to_date)

    if officer is not None and officer != '':
        fc = Q(selected__gte=fm_date, selected__lte=to_date, selected_by_id=officer)

    if state is not None and state != '':
        fc &= Q(sub_state_id=state)




    # print(cnic)
    applicant = Applicants.objects.filter(fc).select_related().extra(select={'date':'DATE(tbl_applicant.created)'}).values_list('cnic', 'cnic_insurance_date' ,'gender','marital_status', 'first_name', 'last_name', 'dob', 'contact', 'project__name', 'address', 'city__name', 'source', 'date')


    print(applicant.query)
    print(applicant)
    applicant_list = list(applicant)
    print(applicant_list)
    # """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    # rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    headers = ['CNIC', 'CNIC Insurance Date', 'Gender', 'Marital Status', 'First Name', 'Last Name', 'Date of Birth', 'Contact', 'Project', 'City', 'Address', 'source']
    rows = [('CNIC', 'CNIC Insurance Date', 'Gender', 'Marital Status', 'First Name', 'Last Name', 'Date of Birth', 'Contact',
     'Project', 'City', 'Address', 'source')];

    # first_data_row = next(iter(data['results']), None)
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer) # , fieldnames=headers
    pseudo_buffer.write(headers)
    #writer.writeheader(headers);
    writer.writerow(headers);
    rows = ( writer.writerow(row) for row in applicant)

    # rows.insert(0, headers)
     # rows.append(headers);
    # print(rows)

    # response = StreamingHttpResponse(applicant, content_type="text/csv")
    response = StreamingHttpResponse(iter_items(applicant, Echo()), content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="applicant.csv"'
    return response

    #
    # writer.writerow(['CNIC', 'CNIC Insurance Date', 'Gender', 'Marital Status', 'First Name', 'Last Name', 'Date of Birth', 'Contact', 'Project', 'City', 'Address', 'source', 'Apply Date'])
    #
    # for row in applicant_list:
    #     writer.writerow(
    #             ['row.cnic', 'row.cnic_insurance_date', 'row.gender', 'row.marital_status', 'row.first_name', 'row.last_name',
    #              'row.dob', 'row.contact', 'row.project__name', 'row.city__name', 'row.address', 'row.source'])
    #
    # # response = StreamingHttpResponse((writer.writerow(
    # #     ['row.cnic', 'row.cnic_insurance_date', 'row.gender', 'row.marital_status', 'row.first_name', 'row.last_name',
    # #      'row.dob', 'row.contact', 'row.project__name', 'row.city__name', 'row.address', 'row.source']) for row in
    # #                                   applicant_list),
    # #                                  content_type="text/csv")
    #
    # response = StreamingHttpResponse(writer.writerows(applicant), content_type="text/csv")
    # response['Content-Disposition'] = 'attachment; filename="applicant.csv"'
    #
    # return response
def iter_items(items, pseudo_buffer):
    headers = ('CNIC', 'CNIC Insurance Date', 'Gender', 'Marital Status', 'First Name', 'Last Name', 'Date of Birth', 'Contact', 'Project', 'City', 'Address', 'source', 'Applied Date Time')
    writer = csv.writer(pseudo_buffer) #, fieldnames=headers)
    # yield pseudo_buffer.write(headers)
    yield writer.writerow(headers)

    for item in items:
        print(item)
        yield writer.writerow(item)


def setApplicantAssesment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # print(request.user.id);
        creater = Users.objects.filter(id=request.user.id).first()

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
                # del var_applcant.full_name
            else:
                var_applcant = Applicants()

            var_applcant.cnic = data['cnic']
            var_applcant.cnic_insurance_date = data['cnic_insurance_date']

            # datetime.datetime.strptime(data['cnic_insurance_date'],'%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')

            var_applcant.first_name = data['first_name']
            var_applcant.last_name = data['last_name']
            var_applcant.father_name = data['father_name']
            var_applcant.contact = data['contact']

            if data['eaddress'] == '':
                var_applcant.eaddress = 'xyz@rizvan.com'
            else:
                var_applcant.eaddress = data['eaddress']

            var_applcant.gender = data['gender']
            var_applcant.dob = data['dob']
            # datetime.datetime.strptime(data['dob'], '%Y-%m-%dT%H:%M:%S.%f%z').strftime('%Y-%m-%d')
            var_applcant.city_id = data['city_id']
            var_applcant.language_id = data['language_id']
            var_applcant.address = data['address']
            var_applcant.state_name = data['state_name']
            var_applcant.sub_state_id = data['sub_state_id']
            # var_applcant.ApplicantsEducations =
            # if data['typing'] == 'officer':
            #     var_applcant.department_id = data['department_id']
            #     var_applcant.designation_id = data['designation_id']
            #     var_applcant.project_id = data['project_id']

            var_applcant.modified_by = creater
            var_applcant.created = datetime.datetime.now()
            var_applcant.state_id = 287
            var_applcant.sub_state_id = data['sub_state_id']
            # print('before save')

            if data['typing'] == 'head':
                var_applcant.approved = datetime.datetime.now()
                var_applcant.approved_by = creater
            elif data['typing'] == 'manager':
                var_applcant.finalized = datetime.datetime.now()
                var_applcant.finalized_by = creater
            elif data['typing'] == 'officer':
                var_applcant.state_name = "shortlisted"
                var_applcant.selected = datetime.datetime.now()
                var_applcant.selected_by = creater
                var_applcant.department_id = data['department_id']
                var_applcant.designation_id = data['designation_id']
                var_applcant.project_id = data['project_id']
                # else:
                #     var_applcant.selected = datetime.datetime.now()
                #     var_applcant.selected_by = creater

                # print(var_applcant.query)
                # try:p
                var_applcant.save()
            # except OperationalError:
            #     print(connection.queries)

            appExp = Applicants.objects.filter(id=var_applcant.id).first()

            comments = data['comments'];
            if comments:
                acObj = ApplicantsComments(applicant=appExp,
                                           remarks=comments,
                                           status=1,
                                           state_id=287,
                                           sub_state_id=data['sub_state_id'],
                                           created_by=creater)
                print(acObj)
                acObj.save()

            applicant_orientations = data['applicant_orientations']
            if (ApplicantOrientation.objects.filter(applicant_id=var_applcant.id, role=data['typing'])):
                ApplicantOrientation.objects.filter(applicant_id=var_applcant.id).update(status=F('status') + 1,
                                                                                         active=0, modified_by=creater)

            elif (ApplicantOrientation.objects.filter(applicant_id=var_applcant.id)):
                ApplicantOrientation.objects.filter(applicant_id=var_applcant.id).update(active=0, modified_by=creater)

                # ExistingApplicantOrientation = ApplicantOrientation.objects.get(applicant_id=var_applcant.id)
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
                                                  created_by=creater)
                # print(axObj)
                axObj.save()
                # started = datetime.datetime.strptime(ax['started'],
                #                                      '%Y-%m-%dT%H:%M:%S.%f%z').strftime(
                #     '%Y-%m-%d'),
                # ended = datetime.datetime.strptime(ax['ended'],
                #                                    '%Y-%m-%dT%H:%M:%S.%f%z').strftime(
                #     '%Y-%m-%d'),
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
    return JsonResponse({'message': 'Wrong Request ', 'success_status': False}, status=404)
