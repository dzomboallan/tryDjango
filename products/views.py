from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .forms import ProductForm, RawForm
from .models import Product


# Create your views here.
def product_create_view(request):
    my_form = RawForm()

    if request.method == 'POST':
        my_form = RawForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
        else:
            my_form.errors
    context = {
        'form': my_form
     }
    return render(request,'product/form.html',context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)  
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = { }
#     return render(request,'product/form.html',context)


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
    
#     context = {
#         'form': form
#     }
#     return render(request,'product/form.html',context)


def product_detail_view(request):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description' : obj.description,
    #     'price' : obj.price,
    #     'summary' : obj.summary
    # }

    context = {
        'object': obj
    }
    return render(request,'product/detail.html',context)

def rendering_initial_data(request):
    initial_data ={
        'title':'This is an awesome title'
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, initial_data=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request,'product/form.html',context)

def dynamic_lookup_view(request,id):
    #obj = Product.objects.get(id=id)
    #obj = get_object_or_404(Product, id=id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {'obj':obj}
    return render(request,'product/detail.html',context)
