import json, unittest

import app

class TestCases(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def test_without_args(self):
        response = self.app.get("/")

        self.assertEqual(response.status_code, 200)

    def test_with_args(self):
        response = self.app.get("/?weight=50&height=167")
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data["bmi"], 17.93)
        self.assertEqual(data["label"], "underweight")
        self.assertEqual(response.status_code, 200)

    def test_invalid_value(self):
        response = self.app.get("/?weight=0&height=0")
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(data["error"], "float division by zero")

unittest.main()



