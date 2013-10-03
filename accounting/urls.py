from django.conf.urls import patterns, include, url

from views import JournalListView, JournalDetailView, JournalDeleteView, JournalUpdateView, JournalCreateView

urlpatterns = patterns('',
	url(r'journals/(?P<pk>\d+)/update$', JournalUpdateView.as_view(), name="journal_update"),
	url(r'journals/(?P<pk>\d+)/del$', JournalDeleteView.as_view(), name="journal_delete"),
	url(r'journals/(?P<pk>\d+)$', JournalDetailView.as_view(), name="journal_detail"),
	url(r'journals/create$', JournalCreateView.as_view(), name="journal_create"),
	url(r'journals', JournalListView.as_view(), name="journals"),
	url(r'reports', JournalListView.as_view(), name="reports"),
)
