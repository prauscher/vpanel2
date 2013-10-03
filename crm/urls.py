from django.conf.urls import patterns, include, url

from django.views.generic.base import TemplateView

urlpatterns = patterns('',
	url(r'^(?P<pk>\d+)$', TemplateView.as_view(), name="detail")
)
