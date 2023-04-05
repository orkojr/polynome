from somme import *
from scalaire import *

def produitpoly(p,q) :
    """ fonctionn qui prend deux polynome en parametre et retourne le produit de ces
    polynomes"""
    res = []
    for d in range( len(p)):
        res =addPoly(res,scalairepoly(decalepoly(q,d),p[d]))
    return res

#illustration
p = [3,23,4]
q = [3,45,5]
print (produitpoly(p,q))