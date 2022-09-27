n = int(input("digite um numero inteiro :"))
print("digite uma das bases para converção:"
"[1] BINARIO"
"[2] OCTAL"
"[3] HEXADECIMAL")
opcao = int(input("sua opção :"))
if opcao == 1:
    print("{} convertido para BINARIO e {}".format(n, bin(n)[2:]))

elif opcao == 2:
    print("{} convertido para OCTAL e {}".format(n, oct(n)[2:]))

elif opcao == 3:
    print("{} convertido em HEXADECIMAL e {}".format(n, hex(n)[2:]))

else:
    print("por favor escolha uma opção valida.")