vcasa = float(input("qual eo valor da casa ?"))
salario = float(input("qual eo seu salario ?"))
qanos = int(input("em quantos anos vc quer pagar a casa ?"))
prestacao = vcasa/qanos
psalario = salario*0.30

if prestacao <= psalario:
    print("seu emprestimo foi aceito tera que pagar uma prestação de R${}".format(prestacao))

else:
    print("seu imprestimo foi negado a prestação exedeu os 30 porsento seu lario")