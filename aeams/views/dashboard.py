from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
import datetime
from aeams.models import TblUsers as Users, TblDomains as Domains, TblSetups as Setups, TblSetupSetups as setupSetups
from .__init__ import *
from .common import need_domains, need_states

# self.request.user
# def buildTree(elements, parent_id):
# 	branch = []
# parents = { key: value for key, value in elements.items() if(value['sub_setup__parent_id'] = parent_id)}


def index(request, page=None, access=None, permission=None, aptype=None):
    # print(access)
    # print(permission)
    # print(request)
    # print('page')
    # print(page)
    # print('page')
    #if request.session.has_key('is_logged'):
        # print(self.request.user)
        # print(request.user.role_id)

    officerObj = Users.objects.filter(role__slug__contains='_RO_', status=1).values('id', 'name')
    #managerObj = Users.objects.filter(role__slug__contains='_RM_', status=1).values('id', 'name')
    headObj = Users.objects.filter(role__slug__contains='_RH_', status=1).values('id', 'name')
    # traineeObj = Users.objects.filter(role__slug__contains='_AT_', status=1).values('id', 'name')
    # leadObj = Users.objects.filter(role__slug__contains='_AL_', status=1).values('id', 'name')

    stateObj = need_states(aptype)
    dominsObjTree = need_domains(request)

    # lambda Expression With substring
    # stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1).values('id', 'name', 'group', 'slug', 'parent_id', 'status')
    # print(officerObj)
    # print(filter(lambda x: x.id == request.user.id, officerObj))
    # iam_ro = list(filter(lambda x: x['id'] == request.user.id, officerObj))
    # iam_rm = list(filter(lambda x: x['id'] == request.user.id, managerObj))
    # iam_rh = list(filter(lambda x: x['id'] == request.user.id, headObj))
    # iam_at = list(filter(lambda x: x['id'] == request.user.id, traineeObj))
    # iam_al = list(filter(lambda x: x['id'] == request.user.id, leadObj))

    # iamin =  list(map(lambda x: x['id'] == request.user.id, officerObj)) return [false, false]
    # print(iam)
    # print(iamin)
    # print(iam.get('id'))

    # if (iam_ro):
    #     iam = 'officer'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')
    # elif (iam_rm):
    #     iam = 'manager'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RM_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')
    # elif (iam_rh):
    #     iam = 'head'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RH_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')
    # elif (iam_at):
    #     iam = 'trainer'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_AT_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')
    # elif (iam_al):
    #     iam = 'lead'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_AL_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')
    # else:
    #     iam = 'None'
    #     stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id',
    #                                                                                                        'name',
    #                                                                                                        'group',
    #                                                                                                        'slug',
    #                                                                                                        'parent_id',
    #                                                                                                        'status')

    # allStateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1).values('id', 'name',
    # 																					   'group',
    # 																					   'slug',
    # 																					   'parent_id',
    # 																					   'status')
    # print(iam)
    # print(headObj);
    #
    # departmentObj = Setups.objects.filter(base_id=2, status=1).values('id', 'name')
    # designationObj = Setups.objects.filter(base_id=3, status=1).values('id', 'name')
    # projectObj = Setups.objects.filter(base_id=1000, status=1, group='Projects').values('id', 'name')
    #
    # # if
    # # 	_recruiter_
    #
    # orientationObj = Setups.objects.filter(base_id=2500, status=1, slug__contains='_recruiter_').values('id', 'name','group', 'slug', 'parent_id', 'status')
    #
    # citiesObj = Domains.objects.filter(domain_type='City', status=1).values('id', 'name')
    # # citiesData = serializers.serialize('json', [citiesObj, ])
    # # print(citiesData)
    # languagesObj = Domains.objects.filter(domain_type='Language', status=1).values()
    # # languagesData = serializers.serialize('json', [languagesObj, ])
    # educationsObj = Domains.objects.filter(domain_type='Education', status=1).values('id', 'name')
    # # educationsData = serializers.serialize('json', [educationsObj, ])
    # institutesObj = Domains.objects.filter(domain_type='Institutes', status=1).values('id', 'name')
    # # institutesData = serializers.serialize('json', [institutesObj, ])
    # majorsObj = Domains.objects.filter(domain_type='Majors', status=1).values('id', 'name')
    # # majorsData = serializers.serialize('json', [majorsObj, ])
    # #
    # print(self.dominsObjTree)

    return render(request, 'setups/index_angularjs.html',
                  context={'variable': 'settings_setups',
                           'role': aptype,
                           'currDate': datetime.datetime.now(),
                           'access': list(access),
                           'domains': list(dominsObjTree),
                           'officers': list(officerObj),
                           'heads': list(headObj),
                           'states': list(stateObj)
                           })

    # ,{'main_access':Maincontrol.objects.filter(role_id_id=request.user.roles_id)})
    # else:
    #     return redirect('login')


