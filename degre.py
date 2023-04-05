
def deg(p) :
    """ fonction qui retourne le degre d'un polynome"""
    if p==[]:
        print("ce polynome est nul")
    return len(p)-1


#illustration du degre
p = [2,34,6,1]
print (deg(p))
