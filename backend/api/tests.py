import json
from django.http import response
from django.test import TestCase

# Create your tests here.


class ListAPITest(TestCase):
    base_url = "/api/"

    def test_get_returns_json_200(self):
        response = self.client.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['content-type'], 'application/json')
        self.assertEqual(json.loads(response.content.decode('utf8')),
                         {"msg": "Hello world"}
                         )
