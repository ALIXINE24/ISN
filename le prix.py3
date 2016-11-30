print("Quel est le prix sans taxes ?")
x = float(input())
x=x+(9.5*x/100)
print "Le prix est ", x ,"Euro"
if x < 120:
  print("Commande passee")
else:
  while x>120:
   print("Quel est le prix sans taxes ?")
   x = float(input())
   x=x+(9.5*x/100)
   print "Le prix est ",x ,"Euro"
   print "Ce prix est trop chere!"
  print "Commande passee"
