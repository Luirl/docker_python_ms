import unittest
import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.main import application


class MultiplyTest(unittest.TestCase):
    def setUp(self):
        application.testing = True
        self.client = application.test_client()

    def test_multiply_ok(self):
        post_data = json.dumps({"number":"100"})
        response = self.client.post('/v1.0/MultiplyBy/5',
                                    data=post_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json', response.content_type)
        self.assertEqual(response.charset, 'utf-8')

        content = response.data

        ok_content = b'{"number": 100, "factor": 5, "result": 500}\n'

        self.assertEqual(content, ok_content)

    def test_multiply_no_number_tag(self):
        post_data = json.dumps({"xxx": "yyy"})
        response = self.client.post('/v1.0/MultiplyBy/5',
                                    data=post_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)

    def test_multiply_no_number_value(self):
        post_data = json.dumps({"number": "yyy"})
        response = self.client.post('/v1.0/MultiplyBy/5',
                                    data=post_data,
                                    content_type='application/json')

        self.assertEqual(response.status_code, 400)
