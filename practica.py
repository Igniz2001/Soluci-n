n = [[1,2,3],[1,2,3],[4,5,6]]

def productoria(m,con = 0, cun = 0, pops = 1, diagonales = []):
    if con == len(m):
        print("los diagonales de la matriz son: ", diagonales)
        print("y la productoria de estos es: ")
        return pops
    else:
        diagonales.append(m[con][cun])
        pops *= m[con][cun]
        return productoria(m, con+1, cun+1,pops)
print(productoria(n))
        
