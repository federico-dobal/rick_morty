from django.test import TestCase
from search.api_request.api_access import ApiAccess
from unittest.mock import MagicMock


class ApiAccessTests(TestCase):
    """
        Tests APIAccess module
    """

    def setUp(self):
        self.api_access = ApiAccess('')

    def test_api_returns_empty_list_characters(self):
        self.api_access.get_query_results = MagicMock(return_value={'data' : {'characters': {'results': []}}})
        self.all_characters = self.api_access.execute_search_all()
        self.assertEquals(self.all_characters, [])

    def test_api_returns_only_rick(self):
        self.api_access.get_query_results = MagicMock(return_value= {'data' : {'characters': {'results': [{'name': 'Rick'}]}}})

        self.all_characters = self.api_access.execute_search_all()

        self.assertEquals(len(self.all_characters), 1)
        self.assertEquals(self.all_characters[0].get('name'), 'Rick')


    def test_api_returns_expected_fields(self):
        self.api_access.get_query_results = MagicMock(return_value= {'data' : {
            'characters': {
                'results': [
                    {
                        'name': 'Rick',
                        'image': 'image_name',
                        'status': 'Dead',
                        'gender': 'M',
                        'species': 'Human'
                    },
                    {
                        'name': 'Morty',
                        'image': 'image_morty',
                        'status': 'Alive',
                        'gender': 'M',
                        'species': 'Human'
                    }
                ]
                }
            }
        })

        self.all_characters = self.api_access.execute_search_all()

        self.assertEquals(len(self.all_characters), 2)

        self.assertTrue(all(['name' in c.keys() for c in self.all_characters]))
        self.assertTrue(all(['image' in c.keys() for c in self.all_characters]))
        self.assertTrue(all(['status' in c.keys() for c in self.all_characters]))
        self.assertTrue(all(['gender' in c.keys() for c in self.all_characters]))
        self.assertTrue(all(['species' in c.keys() for c in self.all_characters]))
