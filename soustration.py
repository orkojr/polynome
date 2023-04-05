
from copiepoly import *

def soustraire(P,Q) :
    """ foction qui effectue la soustraction de deux polynome pris en parametre"""
    res =[]
    res = copiPoly(P,len(Q))
    q = copiPoly(Q,len(P))
    for k in range(len(res)):
        res[k] = res[k]-q[k]
    return res
 #illustration de la soustration de  polynome.   
p = [1,212,4]
q = [2,47,11]
r = soustraire(p,q)
print(r)