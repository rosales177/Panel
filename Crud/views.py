
from django.http import request
from Crud.models import Productos
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from .forms import ProductForm
# Create your views here.
def index(e):
    return render(e,'index.html')

def Crud(e):
    productos = Productos.objects.all()

    context = {'productos':productos}

    return render(e,'crud.html',context)

def Delete(request,id):
    product = get_object_or_404(Productos, cod_product=id)
    if product :
        product.delete()
        return redirect('app:crud')  

def Create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:crud')
    else:
        form = ProductForm()

    context = {'form':form}
    return render(request, 'create.html', context)

def Update(request,id):
    product= get_object_or_404(Productos, cod_product=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance= product)
        if form.is_valid():
            form.save()
            return redirect('app:crud')
    else: 
        form = ProductForm(instance=product)
    context =  {'update': form}
    return render(request, 'update.html', context)



