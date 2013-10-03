from django import forms

from models import Journal

class TransferForm(forms.Form):
	test = forms.CharField()
	pass

class JournalForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ["label", "allowNull"]
