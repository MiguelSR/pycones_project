from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic import ListView

from .models import Author

class AuthorListView(ListView):

    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context
