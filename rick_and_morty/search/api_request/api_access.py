from python_graphql_client import GraphqlClient

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

class ApiAccess():

    #getRickAndMortyApiUrl()
    def __init__(self, url):
        # Instantiate the client with an endpoint obtained from configuration file.
        self.client = GraphqlClient(endpoint=url)

    def get_query_results(self):
        return self.client.execute(query=all_characters_query)

    def execute_search_all(self):
        """
            Searches all the charactesr from GraphQL API.
            It gets name, image, status, gender and species
        """
        # Synchronous request
        data = self.get_query_results()

        # check whether execution was successful
        if data.get('data').get('characters') is not None:
            results = data.get('data').get('characters').get('results')
        else:
            results = []

        return results
