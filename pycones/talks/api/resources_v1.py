from tastypie.resources import ModelResource
from talks.models import Talk


class TalkResource(ModelResource):

    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'patch', 'delete']
        always_return_data = True
