from math import *
def basexenbase10 (bo,snd):
 a=0
 bo=int(input("Entrer la base dans laquelle est le nombre base= "))
 snd=str(input("Quel est le nombre a convertir nombre= "))
 '''[::-1]'''
 for q in range(0,len(snd),+1):
  a=snd[q]*pow(bo,q)
  s=s+a
 return s
def base10enbasex (bv,s):
 o=0
 result=""
 bv=int(input("Entrer la base voulue(entre la base 2 et 10) base= "))
 s=int(input("Entrez le nombre a convertir nombre= "))
 while pow(bv,o)<=s:
  o=o+1 
  '''o-1 est egal au rang max'''
 for p in range(o,0,-1):
  for r in range(bv-1,-1,-1):
   if s-(r * pow(bv,p-1))>=0:
     result=result + str(r)
     s=s-(r * pow(bv,p-1))
     break
 return result
def menu ():
 print("1.Conversion de la base (x) a la base 10") 
 print("2.Conversion de la base 10 a la base (x)")
 print("3.Conversion de la base (x) a la base (x)")
 v=int(input())
 if v==2:
  bv=int(input("Entrer la base voulue(entre la base 2 et 10) base= "))
  s=int(input("Entrez le nombre a convertir nombre= "))
  print (base10enbasex(bv,s))
 elif v==1:
  print("Entrer la base dans laquelle est le nombre")
  bo=int(input(bo=int(input("Entrer la base dans laquelle est le nombre base= "))))
  snd=str(input("Quel est le nombre a convertir nombre= "))[::-1]
  print (basexenbase10(bo,snd))
 elif v==3:
  bo=int(input("Entrer la base dans laquelle est le nombre"))
  snd=str(input("Quel est le nombre a convertir"))[::-1]
  basexenbase10(b,n)
  x=int(input("Entrer la base voulue(entre la base 2 et 10)"))
  print (base10enbasex(x,y))
 else:
  menu()
menu()