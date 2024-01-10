# tests/test_api.py
import json
from app.api import app
import unittest

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_generate_endpoint(self):
        prompt = "Once upon a time"
        response = self.app.post('/generate', data=json.dumps({'prompt': prompt}), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))
        self.assertIn('response', data)
