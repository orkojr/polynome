

def geometriquepolynome(d):
    """ renvoi le developpement limite d'ordre d  en 0 de 1/(1-x)"""
    return [1 for i in range(d+1)]

#illustration

r = geometriquepolynome(5)
print(r)