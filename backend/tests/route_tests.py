import unittest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

class TestAPIRoutes(unittest.TestCase):

    def test_lookups(self):

        response = client.get("/api/v1/lookups")
        self.assertTrue(response.status_code == 200)

    def test_stats(self):

        response = client.get("/api/v1/stats")
        self.assertTrue(response.status_code == 200)
