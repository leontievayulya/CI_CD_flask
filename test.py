from app import app
import unittest


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_success(self):
        r = self.client.get('/add?a=3&b=2') 
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'5.0')


    def test_add_success(self):
        r = self.client.get('/add?a=9&b=2') 
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'11.0')


    def test_add_success(self):
        r = self.client.get('/multi?a=3&b=2') 
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'6.0')


    def test_add_success(self):
        r = self.client.get('/multi?a=5&b=2') 
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.data, b'10.0')


if __name__ == '__main__':
    unittest.main()