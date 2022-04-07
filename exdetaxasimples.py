#Escreva um programa que solicite ao usuário as horas e o valor da taxa por horas para calcular 
# o valor a ser pago por horas de serviço.

horas = int(input ("Digite as horas de serviço realizadas: "))
taxa = float(input ("Digite o valor da taxa por hora: "))
valor = (horas * taxa)
print("As horas são: ", horas)
print("O valor da taxa é: ", taxa)
print("O valor a ser pago é: ", valor)