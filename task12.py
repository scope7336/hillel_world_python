s = input("input your string: ")
inputSym = input("input what find:")
start = -1
while True:
   start = s.find(inputSym, start +1)
   if start == -1:
      break
   print(start)