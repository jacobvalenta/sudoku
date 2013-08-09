from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm

class HomeView(TemplateView):
    template_name = 'home.html'

    # def get_context_data(self, **kwargs):
    #     '''Adds context for the authentication form for inline login'''
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context.update({
    #         'login_form': AuthenticationForm
    #     })
    #     return context
