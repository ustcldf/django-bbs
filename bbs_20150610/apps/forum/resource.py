
# -*- coding: utf-8 -*-
from tastypie import fields
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.constants import ALL_WITH_RELATIONS, ALL

from apps import BaseResource
from apps.district.resource import DistrictResource
from apps.forum.models import Forum

class ForumResource(BaseResource):
    district = fields.ForeignKey(DistrictResource, 'district')
    class Meta:
        queryset = Forum.objects.all()
        resource_name = 'forum'
        authentication = SessionAuthentication()
        authorization = DjangoAuthorization()
        list_allowed_methods = ['post', 'get']
        detail_allowed_methods = []
        always_return_data = True

        filtering = {
            'forum': ALL,
            'name': ALL,
        }