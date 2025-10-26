# tests/test_my_app.py
import unittest
from your_app_code import calculate_sum, is_service_healthy

class TestAppFunctions(unittest.TestCase):

    def test_sum_positive(self):
        # Check if 1 + 2 equals 3
        self.assertEqual(calculate_sum(1, 2), 3)

    def test_service_healthy(self):
        # Check if a 200 status code is considered healthy
        self.assertTrue(is_service_healthy(200))

    def test_service_unhealthy(self):
        # Check if a 404 status code is NOT considered healthy
        self.assertFalse(is_service_healthy(404))

# This part is optional but good practice for running tests locally
if __name__ == '__main__':
    unittest.main()
