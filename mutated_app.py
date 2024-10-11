from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_socketio import SocketIO
from flask import jsonify
from flask_cors import CORS
from configuration.configuration import CORSConfig, AppConfig
app = Flask(__name__)
CORS(app, **CORSConfig.__dict__)
app.config.from_object(CORSConfig)
app.config.from_object(AppConfig)
socketio = SocketIO(app)

def verify_api_key(request):
    api_key = request.headers.get('x-api-key')
    origin = request.headers.get('Origin')
    if api_key and api_key == app.config['API_KEY']:
        if origin and origin in app.config['ORIGINS']:
            return True
        else:
            return False
    return False
app.config['MYSQL_HOST'] = '172.20.0.3'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'example'
app.config['MYSQL_DB'] = 'animals_db'
mysql = MySQL(app)

@app.route('/animals-json')
def get_animals_json():
    if not verify_api_key(request):
        return (jsonify({'error': 'Unauthorized'}), 401)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals')
    data = cur.fetchall()
    animals = []
    for row in data:
        animal = {'id': row[0], 'name': row[1], 'species': row[2], 'weight': row[3]}
        animals.append(animal)
    return jsonify(animals=animals)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    if not verify_api_key(request):
        return (jsonify({'error': 'Unauthorized'}), 401)
    if request.method == 'POST':
        animal_data = request.json
        animalname = animal_data.get('Nombre')
        species = animal_data.get('Especie')
        weight = animal_data.get('Peso')
        if not (animalname and species and weight):
            return (jsonify({'error': 'Falta uno o más campos obligatorios'}), 400)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO animals (animalname, species, weight) VALUES(%s, %s, %s)', (animalname, species, weight))
        mysql.connection.commit()
        flash('Animal Added Successfully')
        return (jsonify({'message': 'Animal added successfully'}), 201)

@app.route('/update/<int:id>', methods=['PUT'])
def update_animal(id):
    if not verify_api_key(request):
        return (jsonify({'error': 'Unauthorized'}), 401)
    if request.method == 'PUT':
        animal_data = request.json
        animalname = animal_data.get('Nombre')
        species = animal_data.get('Especie')
        weight = animal_data.get('Peso')
        if not (animalname and species and weight):
            return (jsonify({'error': 'Falta uno o más campos obligatorios'}), 400)
        cur = mysql.connection.cursor()
        cur.execute('\n            UPDATE animals\n            SET animalname = %s,\n                species = %s,\n                weight = %s\n            WHERE idanimals = %s \n        ', (animalname, species, weight, id))
        mysql.connection.commit()
        flash('Animal Updated Successfully')
        return (jsonify({'message': 'Animal updated successfully'}), 200)

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_animal(id):
    if not verify_api_key(request):
        return (jsonify({'error': 'Unauthorized'}), 401)
    if request.method == 'DELETE':
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM animals WHERE idanimals = %s', (id,))
        mysql.connection.commit()
        flash('Animal Removed Successfully')
        return (jsonify({'message': 'Animal deleted successfully'}), 200)

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals')
    data = cur.fetchall()
    return render_template('index.html', animals=data)
if __name__ == '__main__':
    app.config['ORIGINS'] = ['*']
    print('Configuraciones actuales de Flask:')
    for key, value in app.config.items():
        print(f'{key}: {value}')
    app.run(port=3000, debug=True)