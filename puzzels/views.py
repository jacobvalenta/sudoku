from django.views.generic import TemplateView, ListView, UpdateView, DetailView
from django.contrib.auth.forms import AuthenticationForm
from django.http import Http404
import ast

from .models import Puzzel

class HomeView(TemplateView):
    template_name = 'home.html'

class PuzzelListView(ListView):
    template_name = "puzzel_list.html"
    
    def get_queryset(self, *args, **kwargs):
        return Puzzel.objects.all()
        
class PuzzelView(DetailView):
    template_name = "puzzels/puzzel.html"
    model = Puzzel
    
    def get_object(self, *args, **kwargs):
        try:
            return Puzzel.objects.get(id=self.kwargs['puzzel_id'])
        except Puzzel.DoesNotExist:
            return Http404
            
    def get_context_data (self, *args, **kwargs):
        context = super(PuzzelView, self).get_context_data(*args, **kwargs)
        grid = ast.literal_eval(self.get_object().grid)
        print(grid[0])
        context.update({
            'grid': grid
        })
        return context