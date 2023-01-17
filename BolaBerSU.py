def encontraPares(meninas, meninos, lenmeninas, lenmeninos, pares):
    
    if lenmeninas == 0 or lenmeninos == 0:                              
        print(pares)
    elif abs(meninas[0] - meninos[0]) < 2:                               
        encontraPares(meninas[1:], meninos[1:], lenmeninas - 1, lenmeninos - 1, pares + 1)
    elif meninas[0] < meninos[0]:                                        
        encontraPares(meninas[1:], meninos, lenmeninas - 1, lenmeninos, pares)    
    else:
        encontraPares(meninas, meninos[1:], lenmeninas, lenmeninos - 1, pares)     
                                                                    


if __name__ == '_main_':
    numeroMeninos = int(input())
    meninos = sorted(map(int, input().split()))
    numeroMeninas = int(input())
    meninas = sorted(map(int, input().split()))

    encontraPares(meninas, meninos, numeroMeninas, numeroMeninos, 0)