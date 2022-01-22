from django.shortcuts import render, redirect
from django.views import View 
from django.views.generic import DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client, Product, Ware 

class HomePageView(LoginRequiredMixin, View):  
    def get(self, request):  
        return render(request, 'main/home.html') 

class ClientListCreateView(LoginRequiredMixin, View): 
    def get(self, request):  
        w = Ware.objects.filter(user=request.user).count()
        if w == 0: 
            return redirect("/ware/create/")
        else:
            w = Ware.objects.get(user=request.user)
            cl = Client.objects.filter(ware=w)  
            return render(request, "main/client.html",{"all_clients": cl}) 
