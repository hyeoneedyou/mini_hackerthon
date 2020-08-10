from django.shortcuts import render, redirect, get_object_or_404
from .models import Review

def new(request):
    return render(request, 'review/new.html')


def create(request):
    if request.method == "POST":
        product = request.POST.get('product')
        grade = request.POST.get('grade')
        content = request.POST.get('content')
        user = request.user
        Review.objects.create(product=product, grade=grade, content=content, user=user)
        return redirect('review:main')


def main(request):
    reviews = Review.objects.all()
    return render(request, 'review/main.html', {'reviews':reviews})


def show(request, id):
    review = Review.objects.get(pk=id)
    return render(request, 'review/show.html', {'review': review})


def update(request,id):
    review = get_object_or_404(Review,pk=id)
    if request.method == "POST":
        review.product = request.POST['product']
        review.grade = request.POST['grade']
        review.content = request.POST['content']
        review.save()
        return redirect('review:main')
    return render(request,'review/update.html',{'review':review})


def delete(request, id): 
	review = get_object_or_404(Review, pk=id) 
	review.delete()
	return redirect("review:main")

