def copiPoly(p,n) :
    """ fonction qui prend un polynome et un entier renvoi un polynome de degre max
    l'entier pris en parametre"""
    res = []
    for i in range(len(p)):
        res.append(p[i])
    for i in range(len(p),n):
        res.append(0)
    return res

#ilustration de copipoly

p = [3,4,56,2]
r = copiPoly(p,5)
print(r)
