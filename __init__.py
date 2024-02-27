from flask import Flask, render_template_string, render_template, jsonify
from flask import Flask, render_template, request, redirect
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__) #creating flask app name
db = "sqlite:///database.db"

def get_db_connection():
    connection = sqlite3.connect(db)
    return connection

@app.route('/')
def home():
    return render_template("resume_2.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation/")
def ReadBDD():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM message;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route("/ajouter_message/", methods=['GET', 'POST'])
def ajouter_message():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        message = request.form['msg']
        
        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO message (email, msg) VALUES (?, ?)', (email, message))
            conn.commit()
        except sqlite3.Error as e:
            return f'Error connecting to database: {e}'
        finally:
            conn.close()

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('/consultation/'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('ajouter_message.html')

if(__name__ == "__main__"):
    app.run()
