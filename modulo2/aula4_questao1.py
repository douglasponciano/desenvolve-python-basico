#1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

#O terreno possui 250m2 e custa R$512,490.50

#Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2

#Entrada
comprimento = int(input("Digite o comprimento"))
largura = int(input("Digite a Largura:"))
preco_m2 = float (input("valor do m2:"))

#processamento
area= comprimento * largura #m2 
preco_total = area * preco_m2

#saida
print(f"O terreno possui {area}m2 e custa R${preco_total:,.2f}")