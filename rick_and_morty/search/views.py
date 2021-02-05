from django.shortcuts import render
from search.api_request.api_access import execute_search

#def search(request):
#    return render(request, 'search.html', {})

def home(request):
    return render(request, 'home.html', {})

def search(request):
    srh = request.GET['query']
    #products = product.objects.filter(name__icontains=srh)
    #params = {'products': products, 'search':srh}
    results = execute_search(srh)
    params = {'products': results, 'status': 'Not found' if len(results) == 0 else None}

    return render(request, 'search.html', params)
