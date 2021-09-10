from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
# from django.http import HttpResponse
from django.contrib.auth import logout
import datetime
import logging
import re
from aeams.models import TblUsers as Users, TblDomains as Domains, TblSetups as Setups, TblSetupSetups as setupSetups

EXEMPT_URLS = [settings.LOGIN_URL]
#EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [url for url in settings.LOGIN_EXEMPT_URLS]
    # EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

logger = logging.getLogger(__name__)

class SettingsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #def process_response(self, request, response):
        print("request")
        print(request)
        print("EXEMPT_URLS")
        print(EXEMPT_URLS)
        print("path_info")
        print(request.path_info)
        # print("reverse")
        # print(reverse('aeams:logout'))
        assert hasattr(request, 'user')
        path = request.path_info
        url_is_exempt = any((url == path) for url in EXEMPT_URLS)
        print(url_is_exempt)
        # .lstrip('/')
        # user = getattr(request, 'user', None)
        # if not request.user.is_authenticated():
        #     if True:
        #         return redirect(settings.LOGOUT_URL)
        print(request.user.is_authenticated)
        if path == '/' or path == '': #reverse('aeams:logout'):
            return None
        if path == '/aeams/logout': #reverse('aeams:logout'):
            logout(request)

        if request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)

        # print(self.request.user)
        # print(request.user.role_id)

        self.accessObjTree = need_access(request)
        print(self.accessObjTree)

        if (not self.accessObjTree):
            logout(request)

        request.accessObjTree = self.accessObjTree

        self.permissionObjString = need_permission(request)
        print(self.permissionObjString)
        request.permissionObjString = self.permissionObjString

        self.dominsObjTree = need_domains(request)
        print(self.dominsObjTree)
        request.dominsObjTree = self.dominsObjTree
        # return request
        # pass
        return None


    def need_access(self, request):
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

    def need_domains(self, request):
        dominsObj = list(Domains.objects.filter(status=1).values('id', 'name', 'code', 'domain_type', 'domain_id'))
        dominsObjTree = {}
        for a1 in dominsObj:
            if not a1['domain_type'] in dominsObjTree:
                dominsObjTree[a1['domain_type']] = []

            dominsObjTree[a1['domain_type']].append(a1)

        return dominsObjTree