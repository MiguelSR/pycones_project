from django.shortcuts import redirect
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
    fields = ['name', 'description', 'authors']
    success_url = '/talks/'


class TalkUpdate(UpdateView):

    model = Talk
    fields = ['name', 'description', 'authors']
    success_url = '/talks/'


class TalkDelete(DeleteView):

    model = Talk
    success_url = '/talks/'
