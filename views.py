from django.views.generic import TemplateView,View
from django.http import HttpResponseRedirect

from .forms import UserCreationForm

class RegistrationView(TemplateView):
	template_name = "registration/register.html"

	def post(self, request, *args, **kwargs):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			new_user = authenticate(username=request.POST['username'],
									password=request.POST['password1'])
			login(request, new_user)

		return HttpResponseRedirect("/puzzels/")

	def get_context_data(self, **kwargs):
		context = super(RegistrationView, self).get_context_data(**kwargs)
		context.update({
			'form': UserCreationForm(),
		})
		return context