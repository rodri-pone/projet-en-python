#programme qui demande a l'utilisateur d'entrer une annee et renvoie si elle est bissectile ou pas
annee = int(input("Entrer une annee :"))
print(annee)
bissectile = False
if annee % 4 ==0:
    bissectile = True
if annee %100 ==0:
    bissectile = False
if annee %400 ==0:
    bissectile = True
if bissectile :
    print(" cette annee est bissectile ")
else:
     print("Cette annee n'est pas bissectile ")
   
