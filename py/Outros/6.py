import math
x1 = int(input("Digite X: "))
y1 = int(input("Digite Y: "))
x2 = int(input("Digite X: "))
y2 = int(input("Digite Y: "))
           
teste = math.sqrt((x1-x2)^2+(y1-y2)^2)


if teste >= 10:
    print("longe")
else : print("perto")
