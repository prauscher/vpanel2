from django.conf.urls import patterns, include, url
from django.views.generic.list import ListView

from models import Contact

urlpatterns = patterns('',
	url(r'^$', ListView.as_view(model = Contact), name="start")
)
        
