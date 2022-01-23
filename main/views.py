from django.shortcuts import render, redirect
from django.views import View 
from django.views.generic import DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.urls import reverse_lazy
from .models import Client, Product, Ware, Stats 
from django.contrib import messages
# Homepage
class HomePageView(LoginRequiredMixin, View):  
    def get(self, request):  
        return render(request, 'main/home.html') 


#client
class ClientListCreateView(LoginRequiredMixin, View): 
    def get(self, request):  
        w = Ware.objects.filter(user=request.user).count()
        if w == 0: 
            return redirect("/ware/create/")
        else:
            w = Ware.objects.get(user=request.user)
            cl = Client.objects.filter(ware=w)  
            return render(request, "main/client.html",{"all_clients": cl}) 
    
    def post(self, request): 
        w = Ware.objects.get(user=request.user) 
        Client.objects.create(
            full_name=request.POST.get('new-product-name'),  
            shop_name=request.POST.get('new-product-shop_name'),
            telephone_number=request.POST.get('new-product-telephone_number'), 
            location=request.POST.get('new-product-location'), 
            ware=w
        )
        return redirect('/clients/')  

class ClientUpdateView(LoginRequiredMixin, View):  
    def get(self, request,pk):  
            cl = Client.objects.filter(id=pk)  
            return render(request, "main/client_update.html",{"all_clients": cl}) 
    
    def post(self, request, pk):
            w = Ware.objects.get(user=request.user)
            client = Client.objects.get(id=pk)
            client.full_name=request.POST.get("client_name")
            client.shop_name=request.POST.get("client_shop")
            client.telephone_number=request.POST.get("client_tel")
            client.location=request.POST.get("client-location")
            client.ware=w 
            client.save()
            client.save()
            return redirect("/clients/")
    

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    context_object_name = 'all_clients'
    success_url = reverse_lazy('clients-list-create')


#Product 
class ProductListCreateView(LoginRequiredMixin, View): 
    def get(self, request):  
        w = Ware.objects.filter(user=request.user).count()
        if w == 0: 
            return redirect("/ware/create/")
        else:
            w = Ware.objects.get(user=request.user)
            pr = Product.objects.filter(ware=w)  
            return render(request, "main/products.html",{"all_products": pr}) 
    
    def post(self, request): 
        w = Ware.objects.get(user=request.user) 
        Product.objects.create(
            name=request.POST.get('pr_name'),  
            brand=request.POST.get('pr_brand'),
            price=request.POST.get('pr_price'), 
            in_warehouse=request.POST.get('pr_amount'), 
            ware=w
        )
        return redirect('/products/')  

class ProductUpdateView(LoginRequiredMixin, View):  
    def get(self, request,pk):  
            pr = Product.objects.filter(id=pk)  
            return render(request, "main/product_update.html",{"pr": pr}) 
    
    def post(self, request, pk):
            w = Ware.objects.get(user=request.user)
            pr = Product.objects.get(id=pk)
            pr.name=request.POST.get("name")
            pr.brand=request.POST.get("brand_name")
            pr.price=request.POST.get("price")
            pr.in_warehouse=request.POST.get("amount")
            pr.ware=w 
            pr.save()
            return redirect("/products/")
    

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    context_object_name = 'all_products'
    success_url = reverse_lazy('products-list-create') 


#stats 
class StatsListCreateView(LoginRequiredMixin, View): 
    def get(self, request):  
        w = Ware.objects.filter(user=request.user).count()
        if w == 0: 
            return redirect("/ware/create/")
        else:
            w = Ware.objects.get(user=request.user)
            st = Stats.objects.filter(ware=w)  
            cl = Client.objects.filter(ware=w) 
            pr = Product.objects.filter(ware=w)
            return render(request, "main/stats.html",{"all_stats": st, "clients": cl , "products": pr}) 
    
    def post(self, request): 
        w = Ware.objects.get(user=request.user) 
        cl = request.POST["client"]
        pr = request.POST["product"] 
        t =request.POST['st_total'], 
        p =request.POST['st_payed'], 
        amount = request.POST['pr_amount'],   
        amount1 = Product.objects.get(id=pr)  
        if int(amount[0]) > amount1.in_warehouse or amount1.in_warehouse==0: 
                return messages.warning(request, 'Amount of products are small.')
        else:
                Stats.objects.create(
                    client=Client.objects.get(id=cl),  
                    product=Product.objects.get(id=pr),
                    date=request.POST.get('st_date'),  
                    product_amount= amount[0],
                    total = t[0], 
                    payed= p[0],
                    debt= int(t[0]) - int(p[0]),
                    ware=w) 
                amount1.in_warehouse = int(amount1.in_warehouse) - int(amount[0])
                amount1.save()  
                return redirect('/stats/')   

# class ProductUpdateView(LoginRequiredMixin, View):  
#     def get(self, request,pk):  
#             pr = Product.objects.filter(id=pk)  
#             return render(request, "main/product_update.html",{"pr": pr}) 
    
#     def post(self, request, pk):
#             w = Ware.objects.get(user=request.user)
#             pr = Product.objects.get(id=pk)
#             pr.name=request.POST.get("name")
#             pr.brand=request.POST.get("brand_name")
#             pr.price=request.POST.get("price")
#             pr.in_warehouse=request.POST.get("amount")
#             pr.ware=w 
#             pr.save()
#             return redirect("/products/")
    

class StatsDeleteView(LoginRequiredMixin, DeleteView):
    model = Stats
    context_object_name = 'all_stats'
    success_url = reverse_lazy('stats-list-create')