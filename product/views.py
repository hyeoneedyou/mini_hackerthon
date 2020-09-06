from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Review
from django.contrib.auth.decorators import login_required

def new(request):
    return render(request, 'product/new.html')


def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        writer = request.user
        Product.objects.create(title=title, content=content, price=price, stock=stock, image=image, writer=writer)
        return redirect('product:main')


def main(request):
    products = Product.objects.all()
    return render(request, 'product/main.html', {'products':products})


def show(request, id):
    product = Product.objects.get(pk=id)
    product.view_count += 1
    product.save()
    all_reviews = product.reviews.all().order_by('-created_at')
    return render(request, 'product/show.html', {'product': product, 'reviews':all_reviews})


def update(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == "POST":
        product.title = request.POST['title']
        product.content = request.POST['content']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.image = request.FILES.get('image')
        product.save()
        return redirect('product:show', product.id)
    return render(request,'product/update.html',{'product':product})


def delete(request, id): 
	product = get_object_or_404(Product, pk=id) 
	product.delete()
	return redirect("product:main")

def create_review(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_id)
        current_user = request.user
        review_content = request.POST.get('content')
        Review.objects.create(content=review_content, writer=current_user, product=product)
    return redirect('product:show', product_id)


def update_review(request, review_id): 
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.content = request.POST['content']
        review.save()
        return redirect('product:show', review.product.id)
    return render(request,'product/review_update.html',{'review':review})


def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('product:show', review.product.id) 


@login_required
def product_like(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.user in product.like_user_set.all():
        product.like_user_set.remove(request.user)
    else:
        product.like_user_set.add(request.user)

    if request.GET.get('redirect_to') == 'show':
        return redirect('product:show', product_id)
    else:
        return redirect('product:main')


@login_required
def like_list(request):
    likes = request.user.like_set.all()
    return render(request, 'product/like_list.html', {'likes':likes})
