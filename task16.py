from random import randint

a=[randint(1,50) for _ in range(10)]
list = [ int(s) for s in input().split() ]
k = int(input())
for i in range ( k + 1 , len(list)):
   list[ i - 1 ] = list[ i ]
a.pop()
print(','.join([str(i) for i in list]))