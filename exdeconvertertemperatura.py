#Escreva um programa que solicite ao usuário uma temperatura Celsius, 
# converta para Fahrenheit, e mostre a temperatura convertida

tempc = float(input ("Digite a temperatura em Celsius: "))
tempf = (int(tempc)*9)/5 + 32
print("A temperatura em celsius é: ", tempc)
print("A temperatura em fahrenheit é: ", tempf)