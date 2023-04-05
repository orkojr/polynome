from produit import *

def puissancepoly(p,d):
    """fonctionn qui prend en parametre un ploynome et un entier et eleve le polynome 
    a la puissance de l'entier"""

    res = [1]
    for i in range(d) :
        res = produitpoly(res,p)
    return res


""" illustration"""
p = [3,4,5,6]
r = puissancepoly(p,2)
print(r)