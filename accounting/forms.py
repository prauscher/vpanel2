from django import forms
from django.forms.models import inlineformset_factory

from models import Journal, Record, Split

class TransferForm(forms.ModelForm):
	class Meta:
		model = Record
#		fields = ["voucher", "date"]

TransferSplitFormSet = inlineformset_factory(Record, Split, fk_name="record")

class JournalForm(forms.ModelForm):
	class Meta:
		model = Journal
		fields = ["label", "allowNull"]
