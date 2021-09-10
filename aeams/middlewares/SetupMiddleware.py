from .AlphabetMiddleware import AlphabetMiddleware, EXEMPT_URLS, logger
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
import datetime
from aeams.models import TblSetupSetups as setupSetups

class SetupMiddleware(AlphabetMiddleware):

    def process_view(self, request, view_func, view_args, view_kwargs):
        # print("request")
        # print(view_kwargs)
        # print(view_kwargs.get('page', None))
        # print(view_args)
        # request.META.get('REMOTE_ADDR')
        logger.info(f"Running {view_func.__name__} view")
        # if view_func.func_name == "_shortcircuitmiddleware":
        #     return view_func(request, *view_args, **view_kwargs)
        # print(view_func, view_func.__name__)
        # print("EXEMPT_URLS")
        # print(EXEMPT_URLS)
        # print("path_info")
        # print(request.path_info)
        # print("reverse")
        # print(reverse('aeams:logout'))
        assert hasattr(request, 'user')
        path = request.path_info
        url_is_exempt = any((url == path) for url in EXEMPT_URLS)
        # print(url_is_exempt)
        # .lstrip('/')
        # user = getattr(request, 'user', None)
        # if not request.user.is_authenticated():
        #     if True:
        #         return redirect(settings.LOGOUT_URL)
        # print(request.user.is_authenticated)
        if path == '/' or path == '':  # reverse('aeams:logout'):
            return None
        if path == '/aeams/logout':  # reverse('aeams:logout'):
            logout(request)

        if request.user.is_authenticated:
            self.accessObjTree = self.need_access(request)
            # print(self.accessObjTree)

            if (not self.accessObjTree):
                logout(request)

            view_kwargs["access"] = request.accessObjTree = self.accessObjTree

            self.permissionObjString = self.need_permission(request)
            # print(self.permissionObjString)
            view_kwargs["permission"] = request.permissionObjString = self.permissionObjString
            view_kwargs["aptype"] = request.permissionType = self.need_level(self.permissionObjString)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)

        # print(self.request.user)
        # print(request.user.role_id)
        # return request
        # pass
        # print(view_kwargs)
        return None

    def process_template_response(self, request, response):
        # print(response)
        # print(response.context_data)
        # if not ('notification_count' in response.context_data):
        #     response.context_data['notification_count'] = 2

        accessObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='recruitment', active=1).values(
            'type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug',
            'sub_setup__group', 'sub_setup__id')
        # 'setup_id', 'type', 'sub_setup__name', 'sub_setup__slug', 'sub_setup__group', 'sub_setup__id', 'sub_setup__base_id'
        print(accessObj)

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

        response.context_data['access'] = accessObjTree

        permissionObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='permissions_roles',
                                                   active=1).values(
            'type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug',
            'sub_setup__group', 'sub_setup__id')

        permissionObjString = ""
        for pO in permissionObj:
            permissionObjString += pO['sub_setup__slug']

        response.context_data['permission'] = permissionObjString

        # dominsObj = list(Domains.objects.filter(status=1).values('id', 'name', 'code', 'domain_type', 'domain_id'))
        # dominsObjTree = {}
        # for a1 in dominsObj:
        #     if not a1['domain_type'] in dominsObjTree:
        #         dominsObjTree[a1['domain_type']] = []
        #
        #     dominsObjTree[a1['domain_type']].append(a1)
        #
        # response.context_data['domains'] = dominsObjTree

        return response


    def need_access(self, request):
        accessObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='recruitment', active=1).values(
            'type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug',
            'sub_setup__group', 'sub_setup__id')
        # 'setup_id', 'type', 'sub_setup__name', 'sub_setup__slug', 'sub_setup__group', 'sub_setup__id', 'sub_setup__base_id'
        # print(accessObj)

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

        return accessObjTree

    def need_permission(self, request):
        permissionObj = setupSetups.objects.filter(setup_id=request.user.role_id, type='permissions_roles',
                                                   active=1).values(
            'type', 'sub_setup__parent_id', 'sub_setup__base_id', 'sub_setup__name', 'sub_setup__slug',
            'sub_setup__group', 'sub_setup__id')

        permissionObjString = ""
        for pO in permissionObj:
            permissionObjString += pO['sub_setup__slug']

        return permissionObjString

    def need_level(self, pos):
        type = '_RO_'
        # if pos.find('_RO_') != -1:
        #     type = '_RO_'
        if pos.find('_RE_') != -1:
            type = '_RE_'
        elif pos.find('_RM_') != -1:
            type = '_RM_'
        elif pos.find('_RH_') != -1:
            type = '_RH_'
        elif pos.find('_AT_') != -1:
            type = '_AT_'
        elif pos.find('_AL_') != -1:
            type = '_AL_'

        return type

