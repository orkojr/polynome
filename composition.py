
from puissance import *



def compositionpoly(p,q):
    """fonctionn qui prend deux polynome p et q en parametre et renvoi
    poq"""
    res= []
    for i in range (len(p)):
        res = addPoly(res,scalairepoly(puissancepoly(q,i),p[i]))

    return res

#illustration de la fonction compositionpoly

p = [3,5,765,34]
q = [545,2,45]
r = compositionpoly(p,q)
print(r)