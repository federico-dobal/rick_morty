from django.shortcuts import render
from search.api_request.api_access import ApiAccess
from search.config_reader.config_reader import getRickAndMortyApiUrl


def search(request):
    """
        Implements search view by accessing the Rick and Morty API provided
        by ApiAccess class
    """

    api_access = ApiAccess(getRickAndMortyApiUrl())
    
    params = {'products': api_access.execute_search_all()}

    return render(request, 'search.html', params)
