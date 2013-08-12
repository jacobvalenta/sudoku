from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm

class HomeView(TemplateView):
    template_name = 'home.html'

class PuzzelListView(ListView):
    template_name = "puzzel_list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Puzzel.objects.all()
        