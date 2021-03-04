from random import randint
s = [randint(1,100) for _ in range (15)]
print(", ".join( str(e) for e in s))
k = int(input("Enter your symbol: "))
for i in range (k - 1 , len(s)):
   s [i-1] = s[ i ]
s.pop()
print(','.join([str(i) for i in s ]))