n = 7
a = [[(1)*(j%2==0) for i in range(n)] for j in range(n)]
for r in a:
        print(*r)