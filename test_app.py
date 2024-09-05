import unittest
from App import app, mysql

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Activa la aplicación antes de cada prueba
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

        # Crea contexto de aplicación
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_animals_json(self):
        response = self.client.get('/animals-json', headers={'x-api-key': 'your_secret_api_key'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'animals', response.data)

    def test_add_animal(self):
        response = self.client.post('/add_animal', json={
            'Nombre': 'Leon',
            'Especie': 'Felino',
            'Peso': 180
        }, headers={'x-api-key': 'your_secret_api_key'})
        self.assertEqual(response.status_code, 201)

    def test_update_animal(self):
        response = self.client.put('/update/1', json={
            'Nombre': 'Tigre',
            'Especie': 'Felino',
            'Peso': 200
        }, headers={'x-api-key': 'your_secret_api_key'})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()