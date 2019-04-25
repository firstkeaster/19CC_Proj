from django.conf.urls import url

from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
import os
from sampsite.views import hello_world, root_page, random_number

## add namespace
app_name = 'polls'

basedir = os.path.abspath('') + '/polls'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^t34/$', views.t34Tank),
    ## (?P<question_id>[0-9]+): ?P<> means the parameter name.
    ## then the [0-9]+ means pattern.
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^plots/(?P<maxSize>[0-9]+)/$', views.testPlotter, name='plots'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': \
                basedir + '/images'}, name='image'),
]