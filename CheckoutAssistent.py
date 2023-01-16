import math

itens = int(input())

custo = [ float() * (itens+1)]
custo[0] = 0

for i in range(itens):
    tempo, preco = map(int, input().split())
    
    for j in range(itens-1, -1, -1):
        minimo = min(j + tempo + 1, itens)
        custo[minimo] = min(custo[minimo], custo[j]+preco)

print(custo[itens])