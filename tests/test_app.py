import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_item(self):
        response = self.app.post('/add', json={
            "name": "Test Item",
            "description": "Test Description"
        })
        self.assertEqual(response.status_code, 200)

    def test_get_items(self):
        response = self.app.get('/items')
        self.assertEqual(response.status_code, 200)

    def test_update_item(self):
        # This would require a real MongoDB item to update
        # Placeholder for now
        pass

    def test_delete_item(self):
        # Same, placeholder
        pass

if __name__ == '__main__':
    unittest.main()
