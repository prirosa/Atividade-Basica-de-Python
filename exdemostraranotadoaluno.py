#Escreva um programa que peça por uma pontuação entre 0.0 e 1.0. 
# Se a pontuação for fora do intervalo, mostre uma mensagem de erro. 
# Se a pontuação estiver entre 0.0 e 1.0, mostre a respectiva nota usando a seguinte tabela

try:
    pontuacao = float(input ("Digite a pontuação entre 0.0 e 1.0: ")) 
    if (pontuacao <= 1 and pontuacao >=0):
        if pontuacao >= 0.9:
            print ("A nota é A")
        if pontuacao == 0.8:
            print ("A nota é B")
        if pontuacao == 0.7:
            print ("A nota é C")
        if pontuacao == 0.6:
            print ("A nota é D")
        if pontuacao < 0.6:
            print("A nota é F")
    else:
        print("Pontuação Inválida")  
except:
    print("Pontuação Inválida")

