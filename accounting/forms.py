from django import forms

from models import Journal

class JournalForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ["label", "allowNull"]
