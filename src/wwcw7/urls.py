from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import RedirectView, TemplateView
from wwcw7.views import TopPage, ProfilePage

urlpatterns = i18n_patterns(
    url(r'^$',                 TopPage.as_view(), name='top-page'),
    url(r'^accounts/',         include('allauth.urls')),
    url(r'^profile/$',         ProfilePage.as_view(), name='profile'),
)  
