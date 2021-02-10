from django.shortcuts import render
from search.api_request.api_access import execute_search_with_filter, execute_search_all

#def search(request):
#    return render(request, 'search.html', {})

def home(request):
    return render(request, 'home.html', {})

def search(request):
    if 'query' in request.GET.keys():
        srh = request.GET['query']
        results = execute_search_with_filter(srh)
    else:
        results = execute_search_all()

    params = {'products': results, 'status': 'Not found' if len(results) == 0 else None}

    return render(request, 'search.html', params)
