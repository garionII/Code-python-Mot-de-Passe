# mot de passe

import random

def indentifiant():
    Identifiant = input("Définir un identifiant : ")
    return(Identifiant)
# Fonction permettant de définir un identifiant

def mot_de_passe():
    Password = input("Définir un mot de passe (utilisez au moins une majuscule, une minuscule, un chiffre et un caractère spécial) : ")
    return (Password)
# Fonction permettant de définir un mot de passe

def random_string(pool, length):
    return ''.join(random.choice(pool) for _ in range(length))
# Fonction permettant de choisir une combinaison aléatoire

Compte_identifiant = indentifiant()
""" 
Renvoie à la première fonction, on demande à l'utilisateur
de choisir un identifiant qu'on enregistre dans une variable.
"""

while True:
    pool = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789*/+-&é-è_çà)(=~#{[]}`|`\\^@,;:!ù^$*?./§%¨£µ€¤'
    chaine = random_string(pool, 12)
    print("Exemple d'un mot de passe résistant : ", chaine)
    # Permet de définir un mot de passe résistant de façon aléatoire avec des caractères simples

    Compte_password = mot_de_passe()
    has_digit = any(c.isdigit() for c in Compte_password)
    has_letter = any(c.isalpha() for c in Compte_password)
    has_special = any(not c.isalnum() for c in Compte_password)
    has_uppercase = any(c.isupper() for c in Compte_password)
    has_lowercase = any(c.islower() for c in Compte_password)
    long_enough = len(Compte_password) >= 8
    """ 
    On demande à l'utilisateur de choisir un mot de passe qu'on enregistre dans une variable, 
    avec plusieurs conditions : au moins un chiffre, une lettre,
    une majuscule, une minuscule, un caractère spécial et 8 caractères minimum.
    """

    if has_digit and has_letter and has_special and long_enough and has_uppercase and has_lowercase:
        print("Mot de passe sécurisé")
        break
    else:
        print("Mot de passe trop faible")
# On vérifie les conditions du mot de passe ; si elles ne sont pas correctes, on redemande un mot de passe

while True:
    identifiant = input("Identifiant : ")
    password = input("Mot de passe : ")
    # On demande à l'utilisateur de rentrer son identifiant et son mot de passe qu'on enregistre dans deux variables

    if Compte_identifiant == identifiant and Compte_password == password:
        print("Connecté")
        break
    else:
        print("Identifiant ou mot de passe incorrect, réessayez")
# On vérifie si l'identifiant et le mot de passe saisis par l'utilisateur correspondent à ceux enregistrés
