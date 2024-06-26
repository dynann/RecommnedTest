from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserCreation
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreation
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    context_object_name = 'signup'