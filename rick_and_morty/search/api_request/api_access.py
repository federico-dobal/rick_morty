from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://rickandmortyapi.com/graphql")

# Create the query string and variables required for the request.
query = """
    query charactersQuery($charactersName: String){
        characters (filter: { name:$charactersName}){
            results {
                name,
                image
            }
        }
    }
"""

def execute_search(charactersName):
    variables = {"charactersName": charactersName}

    # Synchronous request
    data = client.execute(query=query, variables=variables)
    print(data)  # => {'data': {'country': {'code': 'CA', 'name': 'Canada'}}}

    # check whether execution was successful
    print(data.get('status'))
    if data.get('data').get('characters') is not None:
        results = data.get('data').get('characters').get('results')
    else:
        results = []

    return results
