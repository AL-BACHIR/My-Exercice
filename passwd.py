choix="oui" 
while choix!="non":

 password = input("Entrez votre mot de passe : ")

 if len(password) < 8:
     print("Mot de passe faible")
     print("Le mot de passe doit comporter au moins 8 caractères.")
 else:
    
     if not any(char.isupper() for char in password):
         print("Mot de passe faible")
         print("Le mot de passe doit contenir au moins une lettre majuscule.")
         choix=input("voulez vous continuer ?(oui ou non)")
     else:
        
         if not any(char.islower() for char in password):
             print("Mot de passe faible")
             print("Le mot de passe doit contenir au moins une lettre minuscule.")
         else:
            
             if not any(char.isdigit() for char in password):
                 print("Mot de passe faible")
                 print("Le mot de passe doit contenir au moins un chiffre.")
             else:
                 print("Mot de passe fort.")
                 print("Super ")
                 break
