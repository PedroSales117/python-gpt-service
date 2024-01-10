# tests/test_openai_service.py
import unittest
from app.openai_service import generate_text

class OpenAIServiceTestCase(unittest.TestCase):
    def test_generate_text(self):
        prompt = "Once upon a time"
        response = generate_text(prompt)
        self.assertIsInstance(response, str)
