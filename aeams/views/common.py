from aeams.models import TblDomains as Domains, TblSetups as Setups
from django.db.models import Q, F

def need_domains(request=None):
    fc = Q(status=1)
    if request:
        fc &= Q(domain_type=request)

    dominsObj = list(Domains.objects.filter(fc).values('id', 'name', 'code', 'domain_type', 'domain_id'))
    dominsObjTree = {}
    for a1 in dominsObj:
        if not a1['domain_type'] in dominsObjTree:
            dominsObjTree[a1['domain_type']] = []

        dominsObjTree[a1['domain_type']].append(a1)

    return dominsObjTree

def need_states(slug=None):
    fc = Q(status=1, base_id=7, parent_id=287)
    if slug:
        if slug == '_RE_':
            slug = '_RO_'
        fc &= Q(slug__contains=slug)

    return Setups.objects.filter(fc).values('id', 'name', 'group', 'slug', 'parent_id', 'status')

