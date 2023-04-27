n1 = [[12, 7],
      [6, 18]]
n2 = [[13, 12],
      [4, 8]]
c = [[0, 0],
     [0, 0]]

for i in range(len(n1)):
    for j in range(len(n1[0])):
        c[i][j] = n1[i][j] + n2[i][j]
for r in c:
    print(c)
