"""pycones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from tastypie.api import Api

from authors.api import resources_v1 as authors_resources
from authors.views import AuthorList, AuthorCreate, AuthorUpdate, AuthorDelete
from talks.api import resources_v1 as talks_resources
from talks.views import TalkList, TalkCreate, TalkUpdate, TalkDelete
from django.contrib.auth.forms import AuthenticationForm


v1_api = Api(api_name='v1')
v1_api.register(talks_resources.TalkResource())
v1_api.register(authors_resources.AuthorResource())

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'talks.views.home', name='home'),

    url(r'^talks/?$',
        login_required(TalkList.as_view()),
        name="talk_list"),
    url(r'^talks/add/?$',
        login_required(TalkCreate.as_view())),
    url(r'^talks/(?P<pk>\d+)/?$',
        login_required(TalkUpdate.as_view()),
        name="talk_edit"),
    url(r'^talks/(?P<pk>\d+)/delete/?$',
        login_required(TalkDelete.as_view()),
        name="talk_delete"),

    url(r'^authors/?$',
        login_required(AuthorList.as_view())),
    url(r'^authors/add/?$',
        login_required(AuthorCreate.as_view())),
    url(r'^authors/(?P<pk>\d+)/?$',
        login_required(AuthorUpdate.as_view()),
        name="author_edit"),
    url(r'^authors/(?P<pk>\d+)/delete/?$',
        login_required(AuthorDelete.as_view()),
        name="author_delete"),

    url(r'^api/', include(v1_api.urls)),

    url(r'^login/$', 'django.contrib.auth.views.login', {
        'template_name': 'login.html',
        'authentication_form': AuthenticationForm}, 'login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'next_page': '/login'}, 'logout'),
]
