def Mux (x,y,z):
 x=str(input("x est vrai ou faux"))
 if x == "vrai":
  x=bool(1)
 else:
  x=bool(0)
 y=str(input("y est vrai ou faux"))
 if y == "vrai":
  y=bool(1)
 else:
  y=bool(0)
 z=str(input("z est vrai ou faux"))
 if z == "vrai":
  z=bool(1)
 else:
  z=bool(0)
 Mux=bool()
 Mux=(not x and y)or(x and z)
 return Mux

def xor (x,y):
 x=str(input("x est vrai ou faux"))
 if x == "vrai":
  x=bool(1)
 else:
  x=bool(0)
 y=str(input("y est vrai ou faux"))
 if y == "vrai":
  y=bool(1)
 else:
  y=bool(0)
 z=(x or y) and (not(x and y))
 return z

def Med (r,j,b):
 r=str(input("Ruth est là oui ou non"))
 if r == "oui":
  r=bool(1)
 else:
  r=bool(0)
 j=str(input("Jon est là oui ou non"))
 if j == "oui":
  j=bool(1)
 else:
  j=bool(0)
 b=str(input("Bob est là oui ou non"))
 if b == "oui":
  b=bool(1)
 else:
  b=bool(0)
 Med=bool()
 Med=((x or y) and (not(x and y))) or (x and y)
 return Med
