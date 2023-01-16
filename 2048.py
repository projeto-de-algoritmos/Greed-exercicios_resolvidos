def main():
  n = int(input())
  
  for i in range(n):
    q = int(input())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    soma = 0
    final = False

    print(v)
    
    for index in range(q):
      if v[index] <= 2048:
        soma += v[index]
      if soma == 2048:
        final = True
    
    print('YES' if final else 'NO')

main()