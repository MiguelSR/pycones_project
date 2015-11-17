from tastypie.resources import ModelResource
from authors.models import Author


class AuthorResource(ModelResource):

    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'post', 'patch', 'delete']
        always_return_data = True
