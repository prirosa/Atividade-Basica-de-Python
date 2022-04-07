#Reescreva seu programa de pagamento, para pagar ao funcionário 1.5 vezes o valor da taxa horária 
#de pagamento pelo tempo trabalhado acima de 40 horas. Além disso, utilize try e except para tratar 
#possíveis erros de entradas não numéricas, mostrando uma mensagem e saindo do programa 

try:
    horas = int(input ("Digite as horas de serviço realizadas: "))
    taxa = float(input ("Digite o valor da taxa por hora: "))
    if horas >= 40:
        valorExtra = (horas*taxa)*1.5
        print("As horas são: ", horas)
        print("O valor da taxa é: ", taxa)
        print("O valor a ser pago é: ", valorExtra)
    else:
        valor = (horas * taxa)
        print("As horas são: ", horas)
        print("O valor da taxa é: ", taxa)
        print("O valor a ser pago é: ", valor)
    
except:
    print("Erro, por favor utilize uma entrada numérica")

