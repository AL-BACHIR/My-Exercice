
import random
import string

longueur = int(input("Entrez la longueur souhaitée du mot de passe : "))

caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

mot_de_passe = ''.join(random.choice(caracteres) for i in range(longueur))

print("Mot de passe généré :", mot_de_passe)

