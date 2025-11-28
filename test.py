from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_success(self):
        r=self.app.get('/add?a=3&b=2')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')

if __name__ == '__main__':
    unittest.main()