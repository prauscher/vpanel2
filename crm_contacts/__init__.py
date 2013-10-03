from vpanel2.connector import addUrlNamespace, addNavigation
import crm_contacts.urls

addUrlNamespace('crm_contacts/', 'crm_contacts', crm_contacts.urls.urlpatterns)
addNavigation('phone-alt', "Kontakte", dropdown = [ {"url": "crm_contacts:start", "label": "Alle"}, {"url": "crm_contacts:start", "label": "Mitglieder"} ])
