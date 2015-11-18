from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Author


class AuthorList(ListView):

    model = Author

    def get_context_data(self, **kwargs):
        context = super(AuthorList, self).get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        return context


class AuthorCreate(CreateView):

    model = Author
    fields = ['name', 'python_level']
    success_url = '/authors/'


class AuthorUpdate(UpdateView):

    model = Author
    fields = ['name', 'python_level']
    success_url = '/authors/'


class AuthorDelete(DeleteView):

    model = Author
    success_url = '/authors/'
