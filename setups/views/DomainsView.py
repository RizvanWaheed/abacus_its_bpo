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


def set_basic_options(request):
	# if request.session.has_key('is_logged'):
		if request.method == 'POST':
			data = json.loads(request.body)
			creater = Users.objects.filter(id=request.user.id).first()

			# print(data['cnic'])
			# var_applcant = Applicants.objects.get_or_create(cnic=data['cnic'])
			# print(request.body)
			# print(request.META.get('CONTENT-TYPE'))
			# del data['cnic']
			retr = {'message': 'Saved Successfully', 'success_status': True}
			code = 200
			try:
				aocObj = Domains( name=data['name'],
								  code=data['code'],
								  domain_type=data['domain_type'],
								  status=1,
								  domain_id=0,
								  created_by=creater,
								  created=datetime.datetime.now())
				aocObj.save()
			except SuspiciousOperation:
				retr = {'message': 'Failed To Save! Try again', 'success_status': False}
				code = 204
				pass
			return JsonResponse(retr, status=code)
		return JsonResponse({'message': 'Wrong Request ', 'success_status': False}, status=404)
	# else:
	# 	return redirect('login')