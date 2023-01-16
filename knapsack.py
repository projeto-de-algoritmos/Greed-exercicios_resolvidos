casos = int(input())

for _ in range (casos):
  n, w = map(int, input().split())
  weights = list(map(int, input().split()))

  total = 0
  items = 0
  v = []

  for i in range (len(weights)):
    if(weights[i] >= w/2 and weights[i] <= w):
      v = [i+1]
      total = weights[i]
      items = 1
      break
    else:
      if(weights[i] + total <= w):
        total += weights[i]
        items += 1
        v.append(i+1)
    if (total >= w/2):
      break
  
  if(total < w/2):
    print(-1)
  else:
    print(items)
    for c in range(items):
      if(c == items - 1):
        print(v[c])
      else:
        print(v[c], end=' ')