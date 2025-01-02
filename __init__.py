from flask import Flask
from flask import render_template
from flask import json
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return "<h2>Bonjour tout le monde !</h2><p>Pour accéder à vos exerices cliquez <a href='./exercices/'>Ici</a></p>"

@app.route('/exercices/')
def exercices():
    return render_template('exercices.html')
  
#Exercice 2 : Création d'une nouvelle route

@app.route('/contact/')
def MaPremierAPI():
  return render_template("contact.html")
  
#Exercice 4 : Création d'une fonction de calcul

@app.route('/calcul_carre/<int:val_user>')
def carre(val_user):
    return "<h2>Le carré de votre valeur est : </h2>" + str(val_user * val_user)

  
"""
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    return f"<h2>La somme de deux valeurs est : {result}</h2>"
  """

# la fonction permettant de faire la somme de 2 valeurs
@app.route('/somme/<int:valeur1>/<int:valeur2>')
def somme(valeur1, valeur2):
    result = valeur1 + valeur2
    return f"<h2> la somme de {valeur1} et {valeur2} est : {result}</h2>"



                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
