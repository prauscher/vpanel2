from vpanel2.connector import addUrlNamespace, addNavigation
import urls

addUrlNamespace('accounting/', 'accounting', urls.urlpatterns)
addNavigation("euro", "Buchhaltung", dropdown = [ {"url": "accounting:journals", "label": "Kontenrahmen"}, {"url": "accounting:reports", "label": "Reports"} ])
