from django.conf.urls import patterns, include, url

from views import EntityDetailView

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)$', EntityDetailView.as_view(), name="detail")
)
