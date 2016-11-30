b=""
a=open("img.pbm","r")
image = a.read()
lignes=image.split("\n")
for i in range [2:len(lignes):1]:
 if lignes[i][0] =="#":
 else:
  for q in range [0:len(lignes[i]):1]:
   if lignes[i][q] == "1":
    b=b+"0"
   else:
	b=b+"1"
  img2.write((b)+\n)
  


