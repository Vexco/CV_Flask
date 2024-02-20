from flask import Flask, render_template, jsonify
import json
import sqlite3

app = Flask(__name__) #creating flask app name

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

def get_db_connection():
    connection = sqlite3.connect('database.db')
    return connection

@app.route('/lecture/')
def ReadBDD():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM livres').fetchall()
    conn.close()

    # Convertit la liste de livre en un format JSON
    json_posts = [{'id': post['id'], 'title': post['title'], 'content': post['auteur']} for post in posts]

    # Renvoie la réponse JSON
    return jsonify(posts=json_posts)

if(__name__ == "__main__"):
    app.run()
