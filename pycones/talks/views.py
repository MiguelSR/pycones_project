from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Talk

def home(self):
    return redirect('talk_list')

class TalkList(ListView):

    model = Talk

    def get_context_data(self, **kwargs):
        context = super(TalkList, self).get_context_data(**kwargs)
        context['talks'] = Talk.objects.all()
        return context


class TalkCreate(CreateView):

    model = Talk
    fields = ['name', 'description']
    success_url = '/talks/'


class TalkUpdate(UpdateView):

    model = Talk
    fields = ['name', 'description']
    success_url = '/talks/'

class TalkDelete(DeleteView):

    model = Talk
    success_url = '/talks/'
