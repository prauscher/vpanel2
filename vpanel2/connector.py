def addUrlNamespace(urlRoot, urlNamespace, urlpatterns):
	from django.conf.urls import patterns, include, url
	import urls

	urls.urlpatterns += patterns('',
		url(urlRoot, include(urlpatterns, namespace=urlNamespace))
	)

navigationElements = []

def addNavigation(icon, label, url = "", dropdown = []):
	"""
	Add a new item to main navigation bar. Either specify the url-name or a list of dropdown-links. This is not recursive
	"""
	navigationElements.append( {"icon": icon, "label": label, "url": url, "dropdown": dropdown} )

def NavigationContext(request):
	return {'navigation': navigationElements}
