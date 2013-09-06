from crm_contacts.models import NaturalPerson, ArtificialPerson, TelephoneNumber, Email
from django.contrib import admin

admin.site.register(NaturalPerson)
admin.site.register(ArtificialPerson)
admin.site.register(TelephoneNumber)
admin.site.register(Email)
