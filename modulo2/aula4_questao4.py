# Lê o valor inteiro referente à quantia em reais
valor = int(input())

# Calcula a quantidade de notas para cada valor possível
notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []
for nota in notas:
    qtd_notas = valor // nota
    quantidades.append(qtd_notas)
    valor -= qtd_notas * nota

# Imprime a quantidade de notas para cada valor possível
for i in range(len(notas)):
    print("{} nota(s) de R${:,.2f}".format(quantidades[i], notas[i]))