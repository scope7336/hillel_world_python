
listNeib = input().split()
counterNeib = 0
for i in range ( 1 , len(listNeib) -1):
   if int(listNeib [i - 1]) < int(listNeib[i]) > int(listNeib[i + 1]):
      counterNeib += 1
   print("neib: {}".format (counterNeib) )
