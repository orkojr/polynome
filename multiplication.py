""" module permettant d'effectuer des multiplications sur les polynomes"""

def coef(p,d) :
    """return le coeficaint de degre d"""
    if(d < len(p)) :
        return p[d]
    else :
        return 0


def comb_lin(p,q,a=1) :
    """ calcule la combinaison lineaire p+a*q
    ou p et q sont des polynomes  et a est un nombre qui prend la valeur 1 par defaut"""
    m = max(len(p),len(q))
    return [coef(p,i)+a*coef(q,i) for i in range(m)]

def multipli_poly(p,q) :
    """ fonction qui  effectue la multiplication de deux polynone pris en parametre"""
    if p == [] or q == [] : return []
    if len(p) == 1 : return [p[0]*k for k in q]
    if len(q) ==1 : return [q[0]*k for k in p]
    k=min(len(p),len(q))//2
    A=p[:k]
    B=p[k:]
    C=q[:k]
    D=q[k:]
    BD = multipli_poly(B,D)
    ABCD = multipli_poly(comb_lin(A,B),comb_lin(C,D))#calcul de (A+B)(C+D)
    AC = multipli_poly(A,C)
    R1 = ([0]*(2*k) +BD) # c'est a dire B*D*x**(2*k)
    R2 = ([0]*k+ABCD)# calcul B*D*x**k
    R = comb_lin(R1,R2,-1)
    ABCD = [0]*k+ABCD #c'est a dire (A+B)*(C+D)*x**k
    R = comb_lin(R,ABCD)
    AC = comb_lin(AC,[0]*k+AC,-1) #c'est a dire le produit  A*C(1-X**k)
    return comb_lin(R,AC)


""" illustration """
p=[1,1,23,4]
q=[1,1,2]
r=multipli_poly(p,q)
print(r)
   