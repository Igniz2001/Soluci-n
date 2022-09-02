
n = [[22,45,67,89],[2,4,6,7],[32,4,5,6],[76,32,76,65]]

def productoria(m,con = 0, cun = 0, pops = 0):
    if con == len(m):
        return pops
    else:
        pops += m[con][cun]
        return productoria(m, con+1, cun+1,pops)
print(productoria(n))
        
