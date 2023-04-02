from django.shortcuts import render , redirect ,get_object_or_404
from django.views import View
from .models import Products
from django.db.models import Count
from . forms import CustemRegistrationForm ,CustemProfileForm
from django.contrib import messages
from .models import custem ,Cart,Order
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def LikeView(request , pk):
    
    product = Products.objects.get(pk=pk)

    if request.user in product.likes.all():
        product.likes.remove(request.user)
        
    else:
        product.likes.add(request.user)
    return redirect(reverse("detail" ,kwargs={"pk":pk}))



def home(request):
    
    return render(request,"site/home.html")

def aboute(request):
    
    return render(request,"site/aboute.html")


def contact(request):
    
    return render(request,"site/contact.html")

class CategoryView(View):
    
    def get(self,request,val):
        product = Products.objects.filter(category=val)
        title = Products.objects.filter(category=val).values('title')
        return render(request,"site/category.html",locals())


class DetailView(View):
    
    def get(self,request,pk):

        product = Products.objects.get(pk=pk)

        return render(request,"site/detail.html",locals())


class CustemRegistrationView(View):
    
    def get(self,request):

        form = CustemRegistrationForm()
        
        return render(request,"site/CustemRegistrationForm.html",locals())
    def post(self,request):
        
        form = CustemRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Login! Registration Successfully")
            
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request,"site/CustemRegistrationForm.html",locals())


class ProfileView(View):
    def get(self,request):
        form = CustemProfileForm()
        return render(request,"site/profile.html",locals())

    def post(self,request):
        form = CustemProfileForm(request.POST)
        if form.is_valid():
            
            user = request.user
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            
            reg = custem(user=user,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, "Login! Registration Successfully")
        else:
            messages.warning(request,"Invalid Input Data")

        return render(request,"site/profile.html",locals())


    

def address(request):
    
    add= custem.objects.filter(user=request.user)
    
    
    return render(request,"site/address.html",locals())


class UpdateAddress(View):
    def get(self,request,pk):
        add = custem.objects.get(pk=pk)
        form = CustemProfileForm(instance=add)

        return render(request,"site/UpdateAddress.html",locals())

    def post(self,request,pk):
        form = CustemProfileForm(request.POST)
        if form.is_valid():
            
            add = custem.objects.get(pk=pk)
            add.user = request.user
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request, "Updated")
        else:
            messages.warning(request,"Invalid Input Data")

        return redirect("address")




# panner (0)
def add_to_cart(request ,pk):
    
    user = request.user
    product = get_object_or_404(Products,pk=pk)
    
    cart , _ = Cart.objects.get_or_create(user=user)
    
    order , created = Order.objects.get_or_create(user=user,ordred=False,product=product)
    
    
    if created:
        cart.orders.add(order)
        cart.save()
    
    else:
        order.quantity += 1
        order.save()
        
    return redirect(reverse("detail" ,kwargs={"pk":pk}))
    
    
    
def cart(request):
    
    cart = get_object_or_404(Cart,user=request.user)
    
    return render(request, "site/cart.html",context={'orders':cart.orders.all()})
    
    
@login_required
def cart_delete(request):
     
    if cart := request.user.cart:
        cart.delete()

    return redirect('home')
        
    
    
    
    