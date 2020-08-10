from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def new(request):
    return render(request, 'product/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        user = request.user
        Product.objects.create(title=title, content=content, price=price, stock=stock, image=image, user=user)
        return redirect('product:main')


def main(request):
    products = Product.objects.all()
    return render(request, 'product/main.html', {'products':products})


def show(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'product/show.html', {'product': product})


def update(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == "POST":
        product.title = request.POST['title']
        product.content = request.POST['content']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('product:main')
    return render(request,'product/update.html',{'product':product})


def delete(request, id): 
	product = get_object_or_404(Product, pk=id) 
	product.delete()
	return redirect("product:main")

