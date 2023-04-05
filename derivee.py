

def derivee(p):
    """ fonction qui retourne la derivee d'une fonction prise en parametre"""
    p1 = []
    for i in range(1,len(p)):
        p1.append(p[i]*i)
    return p1

# illustration de la derivee
p =[3,45,3,54]
print(derivee(p))

