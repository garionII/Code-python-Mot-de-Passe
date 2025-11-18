#mot de passe

import random

def indentifiant():
    Identifiant = input("Définir un identifiant : ")
    return(Identifiant)
#fonction permettant de définir un identifiant

def mot_de_passe():
    Password = input("Définir un mot de passe (utilisez au moins une majuscule, une minuscule, un chiffre et un caractère spécial) : ")
    return (Password)
#fonction permettant de définir un mot de passe

def random_string(pool, length):
    return ''.join(random.choice(pool) for _ in range(length))
#fonction permettant de choisir une combinaison aléatoire

Compte_identifiant = indentifiant()
""" 
    renvoie à la première fonction, on demande à l'utilisateur
    de choisir un identifiant qu'on enregistre dans une variable

"""
while True:
    pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedefghijklmnopqrstuvwxyz0123456789*/+-&é-è_çà)(=~#{[]}`|`\^@,;:!ù^$*?./§%¨£µ€¤'
    chaine = random_string(pool, 12)
    print("Exemple d'un mot de passe résistant : ",chaine)
    #permet de définir un mot de passe résistant de façon aléatoire avec de simple caractères

    Compte_password = mot_de_passe()
    has_digit = any(c.isdigit() for c in Compte_password)
    has_letter = any(c.isalpha() for c in Compte_password)
    has_special = any(not c.isalnum() for c in Compte_password)
    has_uppercase = any(c.isupper() for c in Compte_password)
    has_lowercase = any(c.islower() for c in Compte_password)
    long_enough = len(Compte_password) >= 8
    """ 
    on demande à l'utilisateur de choisir un mot de passe qu'on enregistre dans une variable 
    mais avec plusieurs conditions pour ce mot de passe: au moin un chiffre, une lettre, une majuscule,
    une miniscule, un caractère spécial et 8 caractères de long
    """

    if has_digit and has_letter and has_special and long_enough and has_uppercase and has_lowercase:
        print("Mot de passe sécurisé")
        break
    else:
        print("Mot de passe trop faible")
# on verifie les conditions du mot de passe, si elle nes sont pas correcte on redéfinis un mot de passe

while True:
    identifiant = input("Identifiant : ")
    password = input("Mot de passe : ")
# on demande à l'utilisateur de rentrer ses identifiants et mot de passe qu'on enregistre dans 2 variables

    if Compte_identifiant == identifiant and Compte_password == password:
        print("connecté")
        break
    else:
        print("Identifiant ou mot de passe incorrecte, réessayez")
# on verfifie si l'identifiant et le mot de passe entrer par l'utilisateur sont correcte à ceux enregistrés
   
