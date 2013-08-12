from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from sudoku.puzzels.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
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
