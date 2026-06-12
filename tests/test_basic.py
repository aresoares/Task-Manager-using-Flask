import sys
import unittest
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[1] / "todo_project"
sys.path.insert(0, str(PROJECT_DIR))

from todo_project import app


class BasicRouteTestCase(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_returns_success(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
