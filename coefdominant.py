

def coefDomi(p) :
    """fonction qui retourne le coeficiant  dominant
    d'un polynome non nul. et error sinon"""
    if p ==[]:
        print( "error" )
    else :
        return p[len(p)-1]

#illustration
p = [2,34,6,1]
print (coefDomi(p))