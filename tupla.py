lanche = ("hanburgue", "suco", "pudim", "pizza")

for comida in lanche :
    print(f'eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'vou comer {lanche[cont]} na posição {cont}')

for pos , comida in enumerate(lanche):
    print(f'vou comer {comida} na posição {pos}')

print('comi pra caramba!')