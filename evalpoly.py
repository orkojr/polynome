def evalPoly(p,x) :
    """ fonction qui prend en parametre un polynome p et un reel x et evalue le 
    polynome en fonction de x"""
    res = 0
    v  = 1
    for k in range(len(p)) :
        res = res + p[k]*v
        v = v*x
    return res

#illustration
p=[43,43,2,-66]
r = evalPoly(p,3)#c'est a dire le calcul de p(3)
print(r)