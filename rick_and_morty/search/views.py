from django.shortcuts import render
from search.api_request.api_access import execute_search_all


def search(request):

    results = execute_search_all()

    params = {'products': results, 'status': 'Not found' if len(results) == 0 else None}

    return render(request, 'search.html', params)
