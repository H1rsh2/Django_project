from django.shortcuts import render, redirect
from .models import Stock
from .models import Food
from .forms import StockForm
from .forms import ProviderForm
from .forms import FoodForm
from .models import Provider


def intel(request):
    return render(request, 'main/intel.html')


def signin(request):
    return render(request, 'main/signin.html')


def index(request):
    stocks = Stock.objects.all()
    return render(request, 'main/index.html', {'title': 'Закупки', 'stocks': stocks})


def about(request):
    providers = Provider.objects.order_by()
    return render(request, 'main/about.html', {'title': 'Поставщики', 'providers': providers})


def create_stock(request):
    error = ''
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = StockForm()
    context = {
        'form': form,
        'error':error
    }
    return render(request, 'main/create_stock.html', context)


def create_provider(request):
    error = ''
    if request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('provider')
        else:
            error = 'Форма была неверной'

    form = ProviderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_provider.html', context)


def planning(request):
    return render(request, 'main/planning.html')


def report(request):
    query_results = Food.objects.all()
    form = FoodForm()
    context = {
        'query_results': query_results,
        'form': form,
    }
    return render(request, 'main/report.html', context)