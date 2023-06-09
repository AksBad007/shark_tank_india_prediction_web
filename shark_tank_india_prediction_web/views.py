from django.shortcuts import render
from .model.getPredictions import getPredictions

def home(request):
    return render(request, 'index.html')

def result(request):
    result = getPredictions(
        request.GET['industry'],
        request.GET['y_rev'],
        request.GET['m_rev'],
        request.GET['g_margin'],
        request.GET['n_margin'],
        request.GET['og_ask'],
        request.GET['og_equity'],
        request.GET['og_value'],
        request.GET['patents']
    )
    return render(request, 'result.html', { result })