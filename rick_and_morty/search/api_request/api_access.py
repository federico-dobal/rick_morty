from python_graphql_client import GraphqlClient

# Instantiate the client with an endpoint.
client = GraphqlClient(endpoint="https://rickandmortyapi.com/graphql")

# Create the query string required for the request.
all_characters_query = """
    query charactersQuery{
      characters {
        results {
          name,
          image,
          status,
          gender,
          species
        }
      }
    }
"""

def execute_search_all():
    # Synchronous request
    data = client.execute(query=all_characters_query)

    # check whether execution was successful
    if data.get('data').get('characters') is not None:
        results = data.get('data').get('characters').get('results')
    else:
        results = []

    return results
