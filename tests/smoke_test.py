import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# Complete the function below to test a success in running the application
	def test_prediction_route_success(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200, "Home route did not return 200 OK")
		

	# Complete the function below to test a form is rendered
	def test_get_form(self):
		response = self.client.get('/')
		html = response.get_data(as_text=True)

		# check for typical form elements that should appear.
		self.assertIn("<form", html.lower(), "Form tag not found in response")
		self.assertIn("input", html.lower(), "Input field not found in response")
		
 
if __name__ == '__main__':
	unittest.main()