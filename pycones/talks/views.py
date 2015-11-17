from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.generic import ListView

from .models import Talk

def home(self):
    return redirect('talk_list')

class TalkListView(ListView):

    model = Talk

    def get_context_data(self, **kwargs):
        context = super(TalkListView, self).get_context_data(**kwargs)
        context['talks'] = Talk.objects.all()
        return context
