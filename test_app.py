import unittest
from unittest.mock import patch, MagicMock
from App import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Se configura la bd mockeada
        self.mock_mysql = patch('App.MySQL').start()
        self.mock_cursor = MagicMock()
        self.mock_mysql.return_value.connection.cursor.return_value = self.mock_cursor

        # Simulacion de datos
        self.mock_cursor.fetchall.return_value = [
            (5, 'Pelusa', 'Gato', '20'),
            (6, 'Nemo', 'Pez', '6'),
            (7, 'Marlin', 'Pez', '5'),
            (9, 'Dory', 'Pez', '12'),
            (11, 'Pelusa', 'Gato', '15'),
            (12, 'Firulais', 'Perro', '21'),
            (13, 'Lifo', 'Gato', '21'),
            (14, 'Fido', 'Perro', '10'),
            (15, 'Leon', 'Felino', '180'),
            (16, 'Leon', 'Felino', '180')
        ]

    def tearDown(self):
        patch.stopall()
        self.app_context.pop()

    def test_get_animals_json(self):
        response = self.client.get('/animals-json', headers={'x-api-key': 'your_secret_api_key'})
        
        # Respuesta
        print('Response JSON:', response.json)

        # Datos esperados
        expected_data = {
            "animals": [
                {"id": 5, "name": "Pelusa", "species": "Gato", "weight": "20"},
                {"id": 6, "name": "Nemo", "species": "Pez", "weight": "6"},
                {"id": 7, "name": "Marlin", "species": "Pez", "weight": "5"},
                {"id": 9, "name": "Dory", "species": "Pez", "weight": "12"},
                {"id": 11, "name": "Pelusa", "species": "Gato", "weight": "15"},
                {"id": 12, "name": "Firulais", "species": "Perro", "weight": "21"},
                {"id": 13, "name": "Lifo", "species": "Gato", "weight": "21"},
                {"id": 14, "name": "Fido", "species": "Perro", "weight": "10"},
                {"id": 15, "name": "Leon", "species": "Felino", "weight": "180"},
                {"id": 16, "name": "Leon", "species": "Felino", "weight": "180"}
            ]
        }
        
        # Verificar que los datos devueltos son los esperados
        self.assertEqual(response.json, expected_data)

if __name__ == '__main__':
    unittest.main()
