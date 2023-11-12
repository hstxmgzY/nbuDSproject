n, m = map(int, input().split())
d = [[0]*n for i in range(m+1)]
d[0][0] = 1
for i in range(1, m+1):
	for j in range(n):
	    d[i][j] = d[i-1][(j+1)%n] + d[i+1][(j-1)%n]
print(d[m][0])