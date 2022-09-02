n = [[1,2,3],[1,2,3],[4,5,6]]

def productoria(m,con = 0, cun = 0, pops = 1):
    if con == len(m):
        return pops
    else:
        pops *= m[con][cun]
        return productoria(m, con+1, cun+1,pops)
print(productoria(n))
        
