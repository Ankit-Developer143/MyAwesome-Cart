from django.shortcuts import render

# Import All The Product from models
from .models import Product,Contact,Orders


# Import Ceil
from math import ceil

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.http import HttpResponse


def index(request):
    products = Product.objects.all()
    print(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(products)
        nSlides = n//4 * ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

        parms = {'allProds': allProds}


    return render(request, 'shop/index.html', parms)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    
    if request.method =="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        # print(desc,name,phone)
        
        #Fetch The Data from admin Page
        contact = Contact(name = name,email = email, phone = phone, desc =desc)
        contact.save()
        
        
    return render(request, "shop/contact.html")


def tracker(request):
    return render(request,'shop/tracker.html')


def search(request):
    return HttpResponse("We Are at search ")


def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodView.html",{'product':product[0]})


def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')