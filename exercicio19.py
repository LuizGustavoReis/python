print('''formar de pagamento:R$
[1] a vista 
[2] a vista cartao
[3]2x no cartao
[4]3x ou mais no cartao
''')


op = int(input(" qual a opção de pagamento ?"))

valor = float(input("quanto vc gasto na loja ?"))
des1 = 0.10*valor
des2 = 0.05*valor



if op == 1:
    print("voce vai gastar R${} Reais".format(valor-des1)) #(preço = 10 / 100)
elif op == 2:
    print("voce vai gastar no cartao a vista R${} Reais".format(valor-des2))
elif op == 3:
    print("ate duas vezes sera pago R${} Reais".format(valor/2))
elif op == 4:
    par =int(input("ate quanto vc quer parcelar ?"))
    jur = (valor*0.20)
    v = (jur+valor)/par
    print("vc vai parcelar em {} vai pagar R${} Reais".format(par, v))
else:
    print("escolha uma opção de pagamento valido")