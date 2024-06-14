# Solicita as informações dos produtos e calcula o preço total
total = 0
for i in range(1, 4):
    nome = input("Digite o nome do produto {}: ".format(i))
    preco_unitario = float(input("Digite o preço unitário do produto {}: ".format(i)))
    quantidade = int(input("Digite a quantidade do produto {}: ".format(i)))
    total += preco_unitario * quantidade

# Imprime o preço total formatado
print("Total: R${:,.2f}".format(total))