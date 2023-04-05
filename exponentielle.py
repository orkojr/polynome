

def factoriel(n):
    res =1 
    for i in range(1,n+1) :
        res = res*i
    return res

def exponentielle_polynome(d):
    """ cette fonction renvoie le developpement limite d'ordre d
    en 0 de exponentiellle"""
    res = []
    for i in range( d+1):
        res.append(1.0/factoriel(i))
    return res

#illustration

r = exponentielle_polynome(4)
print(r)