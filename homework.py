"""a =int(input())
b = int(input())
c = int(input())
z = a+b+c
x = z//2
print(x)"""
""""n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit

print('', n2)"""
#print("  ***       *****       ***     *****\n*\t  *\t\t   *\t  *\t    *\t  *\n* *** *\t\t*\t\t  *\t***\t*\t  *\n*\t  *\t\t*****\t  *\t\t*\t  * ")

"""a =int(input())
b = int(input())
c = int(input())
z = a+b+c
x = z//2
print(x)"""
#a = int(input())
#b = int(input())
#c = int(input())
#print(a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2)
"""n1= int(input('введите ваше число' ))
n= ('n1')
n2 = ('n % 10 ')
n3= ('n2 // 10')
n4= ("n3*10+n2*10+n")
print( "" , n4)"""
"""numb= int(input())
numb2 = ( numb // 10)  #12
numb3 =(numb % 10)  #3
numb4 = ( numb2 % 10) #2
n0= (numb //100)
n5=((numb3*10+numb4)*10+n0)
print(n5)"""

"""n1 = int(input())
n = 1
while n ** 2 <= n1:
    print(n ** 2)
    n += 1      """

"""n= int(input("your number"))
n0=2
n1=1
while n0 <= n:
   n0 *= 2
   n1 +=1

   print(n1-1,n0//2)"""
"""x=int(input())
s=0
while x!=0:
    x=int(input())
s+=1
print(x)"""

#задание 13
#x= input("")
#print(x.count(" ")+1)

#задание 10
#x=input("")
#x= x.replace("h","H",x.count("h")-1).replace("H","h",1)
#print(x)


#задание 10
"""str=input()
print(str[2])#a
print(str[-2])#b
print(str[0:5])#c
print(str[:-2])#d
print(str[::2])#e
print(str[1::2])#f
print(str[::-1])#g
print(str[::-2])#h
print(len(str)-1)#i    """


"""inputVal = int(input())
inputCount = 0
inputSum = 0
inputEven = 0
inputOdd = 0
inputMin = inputVal
inputMax = inputVal
while  inputVal != 0:
      inputCount += 1
      inputSum += inputVal
      if inputMin > inputVal:
         inputMin = inputVal
      if inputVal > inputMax:
         inputMax = inputVal
      if inputVal % 2 == 0:
         inputEven += 1
      else:
         inputOdd += 1
      inputVal=int(input())



print( 'Count: {}'.format(inputCount))
print("Sum: {}" . format(inputSum))
print("Average: {}" . format(inputSum / inputCount))
print("min: {}" .format(inputMin))
print("max: {}". format(inputMax))
print("even: {}".format(inputEven))
print("odd: {}".format(inputOdd))"""


#задание 16
from random import randint

a=[randint(1,20) for _ in range(10)]
print(", ".join( repr(e) for e in a))
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(', '.join([str(i) for i in a]))





