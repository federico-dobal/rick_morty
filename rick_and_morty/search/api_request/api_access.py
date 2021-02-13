from python_graphql_client import GraphqlClient
from search.config_reader.config_reader import getRickAndMortyApiUrl


# Instantiate the client with an endpoint obtained from configuration file.
client = GraphqlClient(endpoint=getRickAndMortyApiUrl())

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
    """
        Searches all the charactesr from GraphQL API.
        It gets name, image, status, gender and species
    """
    # Synchronous request
    data = client.execute(query=all_characters_query)

    # check whether execution was successful
    if data.get('data').get('characters') is not None:
        results = data.get('data').get('characters').get('results')
    else:
        results = []

    return results
