a = 4
b = 7
print("a vous de jouer")
x = int(input())
y = int(input())
if (x == a) & (y == b):
 print("coule")
else:
 if (x == a) | y == b:
   print("En vue")
 else:
  while x != a & y != b:
   print("a vous de jouer")
   x = int(input())
   y = int(input())
   if x == a & y == b:
     print("coule")
   else:
     if x == a | y == b:
       print("En vue")
     else:
       print("A l'eau")
   
   
   
   