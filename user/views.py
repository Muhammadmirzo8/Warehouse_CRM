from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login  
from django.views.generic import FormView , CreateView
from django.shortcuts import redirect 
from .models import Ware

class ULoginView(LoginView): 
    template_name = 'user/login.html' 
    fields = '__all__' 
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('clients-list-create') 

class RegisterUserView(FormView):
    template_name = 'user/register.html'  
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('clients-list-create')
    
    def form_valid(self, form): 
        user = form.save() 
        if user is not None: 
            login(self.request, user)
        return super(RegisterUserView, self).form_valid(form)
        
    def get(self, request, *args, **kwargs): 
        if self.request.user.is_authenticated: 
            return redirect('tasks-list')
        return super(RegisterUserView, self).get( request, *args, **kwargs) 

class CreateWareView(LoginRequiredMixin, CreateView): 
    model = Ware  
    fields = ["name", "location", "telephone_number", ]
    success_url = reverse_lazy('home')  
    
    def form_valid(self, form):  
        form.instance.user = self.request.user 
        return super(CreateWareView, self).form_valid(form)

    def get(self, request, *args, **kwargs):  
        w = Ware.objects.filter(user=request.user).count()
        if w > 0 : 
            return redirect('/')
        return super(CreateWareView, self).get( request, *args, **kwargs) 

