
from copiepoly import *

def addPoly(P,Q) :
    """ foction qui additionne deux polynome pris en parametre"""
    res =[]
    res = copiPoly(P,len(Q))
    q = copiPoly(Q,len(P))
    for k in range(len(res)):
        res[k] = res[k]+q[k]
    return res
 #illustration de la somme de deux polynome.   
p = [1,212,4]
q = [2,47,11]
r = addPoly(p,q)
print(r)