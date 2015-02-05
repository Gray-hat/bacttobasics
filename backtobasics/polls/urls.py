from django.conf.urls import url, patterns

from .views import index, detail,vote,results

urlpatterns = [
	#ex: /polls/
	url(r'^$', index,name = 'index'),

	#ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', detail, name = 'detail'),
	url(r'^(?P<question_id>[0-9]+)/results/$',results, name = 'results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$',vote, name = 'vote'),
]