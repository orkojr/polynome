
def scalairepoly(p,n) :
    """ fonction qui retourne le produit scalaire d'un polynome et d'un entier"""
    res= []
    for i in range(len(p)):
        res.append(p[i]*n)
    return res


def decalepoly(p,d):
    """ fonction qui retourne un polynome de degre max len(p) + d et dont les coefficiant de 
    degre inferieur  a  d sont nul si d est positif . et p[-d:len(p)] si d est negatif"""
    
    if d < 0:
        return p[-d:]
    return [0 for i in range(d)] + p


#illustration
p =[2,-4,4]
print(scalairepoly(p,2))
print(decalepoly(p,4))