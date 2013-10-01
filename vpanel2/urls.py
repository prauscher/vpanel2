from django.conf.urls import patterns, include, url

from django.contrib.auth.decorators import login_required
import django.contrib.auth.views
from django.views.generic.base import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^vpanel2/', include('vpanel2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', login_required(TemplateView.as_view(template_name = "vpanel2/dashboard.html")), name="home"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/', django.contrib.auth.views.login, {'template_name': "vpanel2/login.html"}, name="userauth_login"),
    url(r'^logout/', django.contrib.auth.views.logout, {'next_page': "/"}, name="userauth_logout"),
    url(r'^password/done', django.contrib.auth.views.password_change_done, {'template_name': "vpanel2/password_done.html"}, name="userauth_password_change_done"),
    url(r'^password/', django.contrib.auth.views.password_change, {'template_name': "vpanel2/password.html"}, name="userauth_password_change"),
    
)
