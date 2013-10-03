from django.views.generic.detail import DetailView

from models import Entity

class EntityDetailView(DetailView):
	model = Entity
