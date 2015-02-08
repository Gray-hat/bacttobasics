from django.conf.urls import url, patterns

from .views import *

urlpatterns = [
	#ex: /polls/
	url(r'^$', IndexView.as_view(),name = 'index'),

	#ex: /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name = 'detail'),
	url(r'^(?P<pk>[0-9]+)/results/$',ResultsView.as_view(), name = 'results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',vote, name = 'vote'),
]