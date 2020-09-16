from django.shortcuts import render

# Import All The Product from models
from .models import Product,Contact


# Import Ceil
from math import ceil


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