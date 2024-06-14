#2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
#Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:

#86 graus Fahrenheit são 30 graus Celsius.

#Entrada
farenheit= int(input("Digite a Temperatura em F:"))

#processamento
celsius= (farenheit - 32) * (5/9) 


#saida
print(f" {farenheit} graus Farenheit são {celsius:,.2f} graus Celsius:")