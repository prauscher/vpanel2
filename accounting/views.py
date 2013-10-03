from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView

from models import Journal, Account, Record, Split
from forms import JournalForm

class JournalListView(ListView):
	model = Journal
	paginate_by = 20

class JournalDetailView(DetailView):
	model = Journal

class JournalDeleteView(DeleteView):
	model = Journal

class JournalUpdateView(UpdateView):
	template_name = "accounting/journal_form.html"
	form_class = JournalForm

class JournalCreateView(CreateView):
	template_name = "accounting/journal_form.html"
	form_class = JournalForm
