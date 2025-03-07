import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, CI/CD!")

    def test_status_route(self):
        response = self.app.get('/status')
        self.assertEqual(response.status_code, 200)
        self.assertIn("running", response.data.decode())

if __name__ == "__main__":
    unittest.main()
