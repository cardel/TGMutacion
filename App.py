from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_socketio import SocketIO

app = Flask(__name__)

app.config.from_object('configuration.DevConfig')

socketio = SocketIO(app)

#Conexion con la BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'flaskanimals'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals')
    data = cur.fetchall()
    return render_template('index.html', animals = data)

@app.route('/add_animal', methods=['POST'])
def add_animal():
    if request.method == 'POST':
        animalname = request.form['Nombre']
        species = request.form['Especie']
        weight = request.form['Peso']
        print(animalname)
        print(species)
        print(weight)
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO animals (animalname, species, weight) VALUES(%s, %s, %s)',
                    (animalname,species,weight))
        mysql.connection.commit()
        flash('Animal Added Successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_animal(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM animals WHERE idanimals = %s', (id))
    data = cur.fetchall()
    return render_template('edit-animal.html', animal = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_animal(id):
    if request.method == 'POST':
        try:
            animalname = request.form['animalname']
            species = request.form['species']
            weight = request.form['weight']
            
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
            return redirect(url_for('Index'))
        except Exception as e:
            print("Error updating animal:", e)
            flash('Error updating animal')
            return redirect(url_for('Index'))


@app.route('/delete/<string:id>')
def delete_animal(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM animals WHERE idanimals = {0}'.format(id))
    mysql.connection.commit()
    flash('Animal Removed Successfully')
    return redirect(url_for('Index'))
if __name__ == '__main__':
    app.run(port=  3000, debug = True)