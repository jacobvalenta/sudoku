from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sudoku.views.home', name='home'),
    # url(r'^sudoku/', include('sudoku.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
