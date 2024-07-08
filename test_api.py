import unittest
from fastapi.testclient import TestClient
from api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_start_endpoint(self):
        response = self.client.post("/start", json={"url": "http://example.com", "depth": 2})
        self.assertEqual(response.status_code, 200)
        self.assertTrue("status" in response.json())

    def test_status_endpoint(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("status" in response.json())

    def test_results_endpoint(self):
        response = self.client.get("/results")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("results" in response.json())

if __name__ == '__main__':
    unittest.main()
