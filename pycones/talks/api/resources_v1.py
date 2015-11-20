from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from talks.models import Talk


class TalkResource(ModelResource):
    authors = fields.ToManyField(
        'authors.api.resources_v1.AuthorResource',
        'authors', null=True)

    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'patch', 'delete', 'put']
        always_return_data = True
        authorization = Authorization()
