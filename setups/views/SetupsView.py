from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
import datetime
from aeams.models import TblUsers as Users, TblDomains as Domains, TblSetups as Setups, TblSetupSetups as setupSetups
import json
from .__init__ import *
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation

# self.request.user
# def buildTree(elements, parent_id):
# 	branch = []
	# parents = { key: value for key, value in elements.items() if(value['sub_setup__parent_id'] = parent_id)}


def index(request, page=None):
	print('page')
	print(page)
	print('page')
	if request.session.has_key('is_logged'):
		# print(self.request.user)
		# print(request.user.role_id)
		accessObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='recruitment', active=1).values('type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug', 'sub_setup__group', 'sub_setup__id')
		# 'setup_id', 'type', 'sub_setup__name', 'sub_setup__slug', 'sub_setup__group', 'sub_setup__id', 'sub_setup__base_id'
		# print(accessObj)
		if(not accessObj):
			return redirect('/aeams/logout')
		accessObjTree = []
		for aO in accessObj:
			parent = {}
			if (aO['sub_setup__parent_id'] == aO['sub_setup__base_id']):
				parent = aO
				children = []
				for aOl2 in accessObj:
					if(aOl2['sub_setup__parent_id'] == aO['sub_setup__id']):
						children.append(aOl2)
					else:
						pass

				parent['children'] = children
			else:
				pass

			if(bool(parent)):
				accessObjTree.append(parent)

		print(accessObjTree)

		dominsObj = list(Domains.objects.filter(status=1).values('id','name','code','domain_type','domain_id'))
		dominsObjTree = {}
		for a1 in dominsObj:
			if not a1['domain_type'] in dominsObjTree:
				dominsObjTree[a1['domain_type']] = []

			dominsObjTree[a1['domain_type']].append(a1)

		print(dominsObjTree)
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
			stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id', 'name', 'group', 'slug',
																						'parent_id', 'status')
		elif (iam_rm):
			iam = 'manager'
			stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RM_').values('id', 'name', 'group', 'slug',
																						'parent_id', 'status')
		elif(iam_rh):
			iam = 'head'
			stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RH_').values('id', 'name', 'group', 'slug',
																						'parent_id', 'status')
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
			stateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1, slug__contains='_RO_').values('id', 'name', 'group', 'slug',
																						'parent_id', 'status')


		# allStateObj = Setups.objects.filter(base_id=7, parent_id=287, status=1).values('id', 'name',
		# 																					   'group',
		# 																					   'slug',
		# 																					   'parent_id',
		# 																					   'status')
		# print(iam)
		# # print(headObj)
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
		return render(request, 'setups/index_angularjs.html',
					  context={'variable': 'settings_setups',
							   'role': iam,
							   'currDate': datetime.datetime.now(),
							   'access':list(accessObjTree),
							   'domains': dominsObjTree,
							   'officers':list(officerObj),
							   'heads': list(headObj),
							   'states': list(stateObj)
							 })


		#,{'main_access':Maincontrol.objects.filter(role_id_id=request.user.roles_id)})
	else:
		return redirect('login')