from flask import Flask, render_template, request, redirect, url_for, flash
#Importación que permite operar con Flask
from flask_mysqldb import MySQL
#Importación que permite operar con la base de datos MySQL
from flask_socketio import SocketIO
#Importación necesaria para la operación de la App con los archivos configarion
from flask import jsonify
#Importación necesaria para la operación de los Json con la base de datos
from flask_cors import CORS
from configuration.configuration import CORSConfig
#Configuraciones desde el paquete de CORS para tener operadores de configuración más generales

app = Flask(__name__)
CORS(app)
CORS(app, **CORSConfig.__dict__)
app.config.from_object(CORSConfig)
socketio = SocketIO(app)

# Configuración de la API Key
API_KEY = "your_secret_api_key"

def verify_api_key(request): # Authorization
    api_key = request.headers.get('x-api-key')
    if api_key and api_key == API_KEY:
        return True
    return False

#Conexion con la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flaskanimals'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

#GET
@app.route('/animals-json') 
def get_animals_json():
    if not verify_api_key(request): # Verificación de autorización para la petición GET
        return jsonify({'error': 'Unauthorized'}), 401

    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals')
    data = cur.fetchall()

    animals = []
    for row in data:
        animal = {
            "id": row[0],
            "name": row[1],
            "species": row[2],
            "weight": row[3]
        }
        animals.append(animal)

    return jsonify(animals=animals)

#POST
@app.route('/add_animal', methods=['POST'])
def add_animal():
    if not verify_api_key(request): #Verificación de autorizacion para la petición POST
        return jsonify({'error' : 'Unauthorized'}), 401

    if request.method == 'POST':
        # Obtener datos del nuevo animal desde la solicitud
        animal_data = request.json
        animalname = animal_data.get('Nombre')
        species = animal_data.get('Especie')
        weight = animal_data.get('Peso')
        
        # Verificar que se han proporcionado todos los campos necesarios
        if not (animalname and species and weight):
            return jsonify({'error': 'Falta uno o más campos obligatorios'}), 400
        
        # Insertar el nuevo animal en la base de datos
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO animals (animalname, species, weight) VALUES(%s, %s, %s)',
                    (animalname, species, weight))
        mysql.connection.commit()
        flash('Animal Added Successfully')
        return jsonify({'message': 'Animal added successfully'}), 201

#PUT
@app.route('/update/<int:id>', methods=['PUT'])
def update_animal(id):
    if not verify_api_key(request): #Verificación de autorizacion para la petición PUT
        return jsonify({'error' : 'Unauthorized'}), 401

    if request.method == 'PUT':
        # Obtener datos actualizados del animal desde la solicitud JSON
        animal_data = request.json
        animalname = animal_data.get('Nombre')
        species = animal_data.get('Especie')
        weight = animal_data.get('Peso')
        
        # Verificar que se han proporcionado todos los campos necesarios
        if not (animalname and species and weight):
            return jsonify({'error': 'Falta uno o más campos obligatorios'}), 400
        
        # Actualizar el animal en la base de datos
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE animals
            SET animalname = %s,
                species = %s,
                weight = %s
            WHERE idanimals = %s 
        """, (animalname, species, weight, id))

        mysql.connection.commit()  # Confirmar la transacción
        flash('Animal Updated Successfully')
        return jsonify({'message': 'Animal updated successfully'}), 200

#DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_animal(id):
    if not verify_api_key(request): #Verificación de autorizacion para la petición DELETE
        return jsonify({'error' : 'Unauthorized'}), 401

    if request.method == 'DELETE':
        # Eliminar el animal de la base de datos
        cur = mysql.connection.cursor()
        cur.execute('DELETE FROM animals WHERE idanimals = %s', (id,))
        mysql.connection.commit()
        flash('Animal Removed Successfully')
        return jsonify({'message': 'Animal deleted successfully'}), 200

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals')
    data = cur.fetchall()
    return render_template('index.html', animals = data)
if __name__ == '__main__':
    app.run(port=  3000, debug = True)