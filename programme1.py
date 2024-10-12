#programme qui demande les notes d'un etudiant et affiche son grade
float(input(" Entrer votre note de CC :"))
print (CC)
TP =  float(input(" Entrer votre note de TP :"))
print (TP)
EE =  float(input(" Entrer votre note de EE :"))
print (EE)
SUM= CC+TP+EE
if SUM<100 and SUM>=80:
    print(" votre grade est A ")
elif SUM<80 and SUM>=75:
    print(" Votre grade est B+")
elif SUM<75 and SUM>=70:
    print(" Votre grade est B")
elif SUM<70 and SUM>=65:
    print(" Votre grade est B-")
elif SUM<65 and SUM>=60:
    print(" Votre grade est C+")
elif SUM<60 and SUM>=55:
    print(" Votre grade est C")
elif SUM<55 and SUM>=50:
    print(" Votre grade est C-")
elif SUM<50 and SUM>=35:
    print(" Votre grade est D")
elif SUM<35 and SUM>=20:
    print(" Votre grade est E")
elif SUM<20 and SUM>=00:
    print(" Votre grade est F")
else :
    print(" Vous n'avez pas composer!")
