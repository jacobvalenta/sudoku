from django.conf.urls import patterns, include, url
from django.core.urlresolvers import reverse_lazy

from django.contrib import admin
admin.autodiscover()

from sudoku.puzzels.views import HomeView, PuzzelListView, PuzzelView
from .views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^puzzels$', PuzzelListView.as_view(), name="list"),
    url(r'^(?P<puzzel_id>\d+)', PuzzelView.as_view(), name="puzzel"),
    # url(r'^sudoku/', include('sudoku.foo.urls')),

    # Auth
	url(r'^', include(patterns('',
        url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': reverse_lazy('home')}, name="logout"),
        url(r'^', include('django.contrib.auth.urls')),
        url(r'^register/$', RegistrationView.as_view(), name="register"),
    ), namespace='auth')),

	#registration
    # url(r'^register/$', RegistrationView.as_view(), name="register"),

    url(r'^admin/', include(admin.site.urls)),
)
