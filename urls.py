from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from sudoku.puzzels.views import HomeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^sudoku/', include('sudoku.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
