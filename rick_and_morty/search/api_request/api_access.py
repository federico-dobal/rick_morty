from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://rickandmortyapi.com/graphql")

# Create the query string and variables required for the request.
filtered_query = """
    query charactersQuery($charactersName: String){
        characters (filter: { name:$charactersName}){
            results {
                name,
                image
            }
        }
    }
"""

all_characters_query = """
    query charactersQuery{
      characters {
        results {
          name,
          image
        }
      }
    }
"""

def execute_search_with_filter(charactersName):
    print('execute_filter');
    variables = {"charactersName": charactersName}

    # Synchronous request
    data = client.execute(query=filtered_query, variables=variables)
    print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}

    # check whether execution was successful
    print(data.get('status'))
    if data.get('data').get('characters') is not None:
        results = data.get('data').get('characters').get('results')
    else:
        results = []

    return results

def execute_search_all():

    print('execute_search_all');

    # Synchronous request
    data = client.execute(query=all_characters_query)
    print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}

    # check whether execution was successful
    print(data.get('status'))
    if data.get('data').get('characters') is not None:
        results = data.get('data').get('characters').get('results')
    else:
        results = []

    return results
