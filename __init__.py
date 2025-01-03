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
    #return f"<h2> la somme de {valeur1} et {valeur2} est : {result}</h2>"

    # Vérification si la somme est paire ou impaire
    if result % 2 == 0:
        parite = "paire"
    else:
        parite = "impaire"
    
    return f"<h2>La somme de {valeur1} et {valeur2} est : {result} et elle est {parite}.</h2>"

#Exercice 6 : Somme de toutes les valeurs

"""
@app.route('/somme_valeurs/<values>')
def somme_valeurs(values):
    # Diviser les valeurs saisies par des virgules en une liste
    valeurs = values.split(',')
    
    # Convertir chaque élément de la liste en entier
    valeurs_entiers = [int(val) for val in valeurs]
    
    # Calculer la somme de toutes les valeurs
    result = sum(valeurs_entiers)
    
    # Retourner le résultat
    return f"<h2>La somme des valeurs {', '.join(values.split(','))} est : {result}</h2>"
    """

@app.route('/somme_valeurs/<path:values>')
def somme_valeurs(values):
    # Diviser les valeurs saisies par des / en une liste
    valeurs = values.split('/')  # Utiliser '/' comme séparateur
    
    try:
        # Convertir chaque élément de la liste en float pour gérer les entiers, décimaux, et négatifs
        valeurs_floats = [float(val) for val in valeurs]
    except ValueError:
        return "Toutes les valeurs doivent être des nombres valides (entiers, décimaux, ou négatifs).", 400

    # Calculer la somme de toutes les valeurs
    result = sum(valeurs_floats)
    
    # Retourner le résultat formaté
    return f"<h2>La somme des valeurs {' / '.join(valeurs)} est : {result}</h2>"


#Exercice 7 : La valeur la plus importantes

@app.route('/max_valeur/<path:values>')
def max_valeur(values):
    # Diviser les valeurs saisies par des / en une liste
    valeurs = values.split('/')  # Utilisation de '/' comme séparateur pour séparer les valeurs saisies par l'utilisateur
    
    try:
        # Convertir chaque élément de la liste en float pour gérer les entiers, décimaux et négatifs
        # Ici, on utilise une boucle (dans la liste de compréhension) pour parcourir chaque valeur
        valeurs_floats = [float(val) for val in valeurs]
    except ValueError:
        # Si une des valeurs n'est pas convertible en float (par exemple du texte), on renvoie un message d'erreur
        return "Toutes les valeurs doivent être des nombres valides (entiers, décimaux, ou négatifs).", 400

    # Trouver la valeur maximale parmi les valeurs converties
    # La fonction max() est utilisée pour obtenir la plus grande valeur dans la liste 'valeurs_floats'
    max_val = max(valeurs_floats)

    # Retourner le résultat formaté
    # On va afficher les valeurs saisies sous forme de texte, séparées par des virgules
    # Le résultat max est aussi affiché directement sans parenthèses
    return f"<h2>La valeur maximale parmi {', '.join(values.split('/'))} est : {max_val}</h2>"

#Exercice 8 : Mettre un CV en ligne
@app.route('/cv/')
def cv():
    return render_template('cv.html')


                                                                                                               
if __name__ == "__main__":
  app.run(debug=True)
