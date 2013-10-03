from vpanel2.connector import addUrlNamespace
import urls

addUrlNamespace('crm/', 'crm', urls.urlpatterns)
