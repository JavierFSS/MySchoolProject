import math

apaja1 = input().split(" ")
apaja2 = input().split(" ")

x1,y1 = apaja1
x2,y2 = apaja2

pormula = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %pormula)