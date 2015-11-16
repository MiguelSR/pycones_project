from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.generic import ListView

from .models import Talk

# Create your views here.

class TalkListView(ListView):

    model = Talk

    def get_context_data(self, **kwargs):
        context = super(TalkListView, self).get_context_data(**kwargs)
        context['talks'] = Talk.objects.all()
        return context
