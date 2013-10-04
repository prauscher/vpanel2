from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView
from django.views.generic.edit import CreateView, UpdateView, FormView

from models import Journal, Account, Record, Split
from forms import TransferForm, TransferSplitFormSet, JournalForm

class TransferView(CreateView):
	template_name = "accounting/transfer.html"
	form_class = TransferForm

	def form_valid(self, form):
		context = self.get_context_data()
		if context["split_forms"].is_valid():
			self.object = form.save()
			context["split_forms"].instance = self.object
			context["split_forms"].save()
			return super(TransferView, self).form_valid(form)
		
		return super(TransferView, self).form_invalid(form)
		
	def get_context_data(self, **kwargs):
		context = super(TransferView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['split_forms'] = TransferSplitFormSet(self.request.POST)
		else:
			context['split_forms'] = TransferSplitFormSet()
		
		context['journals'] = Journal.objects.all()
		return context

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
