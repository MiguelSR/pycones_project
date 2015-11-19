from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import AuthorForm
from .models import Author
from talks.models import Talk


class AuthorList(ListView):

    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context


class AuthorCreate(CreateView):

    model = Author
    form_class = AuthorForm
    success_url = '/authors/'


class AuthorUpdate(UpdateView):

    model = Author
    form_class = AuthorForm
    success_url = '/authors/'


class AuthorDelete(DeleteView):

    model = Author
    success_url = '/authors/'
