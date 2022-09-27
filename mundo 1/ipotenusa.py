
from math import hypot
co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adijacente: "))
hi = hypot(co,ca)
print("a hipotenusa vai medir{:.2f}".format(hi))
#hi =(co**2+ca**2)**(1/2)
#print("a hipotenusa vai medir {:.2f}".format(hi))

