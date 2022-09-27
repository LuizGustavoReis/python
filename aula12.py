nome =str(input("qual e o seu nome?"))
if nome == "luiz":
    print("seu nome e bonito!")

elif nome == "maria" or nome == "pedro" or nome == "paulo":
    print("seu nome e bem popular no brasil!")

elif nome in "ana claudia jessica juliana":
    print("belo nome femenino!")  

else:
    print("seu nome e bem normal!")    


print("bom dia {}!".format(nome))