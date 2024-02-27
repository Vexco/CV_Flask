from flask import Flask, render_template_string, render_template, jsonify, url_for
from flask import Flask, render_template, request, redirect, session
from flask import json
from urllib.request import urlopen
import sqlite3

app = Flask(__name__) #creating flask app name
db = "database.db"

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

app.secret_key = "c30e18ff-d7e8-4435-a239-65b85f8905a1"

def est_authentifie():
        return session.get('authentifie')

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation/")
def readbdd():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM message;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route("/ajouter_message", methods=['GET', 'POST'])
def ajouter_message():
    try:    
        if request.method == 'POST':
            # Récupérer les données du formulaire
            email = request.form['email']
            message = request.form['msg']
            
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO message (email, msg) VALUES (?, ?)', (email, message))
                conn.commit()
                        
            return redirect(url_for('readbdd'))

            # Rediriger vers la page de consultation des clients après l'ajout

        # Si la méthode est GET, simplement rendre le template du formulaire
        return render_template('ajouter_message.html')
    except Exception as e:
        print("Une erreur est survenue: ", str(e))
        print(traceback.format_exc())
        return str(e), 500
    
@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('readbdd'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

if(__name__ == "__main__"):
    app.run()
