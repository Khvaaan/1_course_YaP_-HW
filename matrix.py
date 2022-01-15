'''
#1
import random

def weight(xin):
	xout = []
	while xin > 0:
		xout.append(random.randint(0, 101))
		xin -= 1
	return xout

ans = []
a, b = input().split()
a , b = int(a), int(b)
while b > 0:
	ans.append(weight(a))
	b -= 1

print(ans)
'''

'''
#2
n = int(input())
ans = 0
for i in range(1, n+1):
	ans += i
print(ans)
'''

'''
#3
n = float(input())
counter = 1
while counter < 15.5:
	print(n, "*", counter, "=", n * counter)
	counter += 0.5
'''

#4
import random

def matrix_el(w): # create matrix 
	ans = []
	for x in range(w): 
		ans.append(random.choice([1, 0]))
	ans.append(0)
	return ans

h,w = input('w h = ').split() # matrix param.
h,w = int(h), int(w) # matrix param.

m = []
ans = 0

# create main matrix 
for i in range(h):
	m.append(matrix_el(w))
m.append([0] * (w + 1))

# expand main matrix
for i in range(h+1):
	m[i][w] = m[i][0]
for j in range(w+1):
	m[h][j] = m[0][j]

for i in range(h+1):
	print(m[i])

for i in range(h):
	for j in range(w):
		ans += m[i][j] * m[i+1][j]
		ans += m[i][j] * m[i][j+1]
print(ans)