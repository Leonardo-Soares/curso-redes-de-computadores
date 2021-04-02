def calculo_media(x1, x2, x3, x4, x5): #Acrescentando 2 variaveis
    media = ((x1 + x2 + x3 + x4 + x5) / 2) #Acrescentando as variaveis criadas
    return media
    
av1 = float(input("Digite o Valor da Av1: "))
av2 = float(input("Digite o Valor da Av2: "))
av3 = float(input("Digite o Valor da Av3: ")) #Variável criada anteriomente para a leitura dos valores
av4 = float(input("Digite o Valor da Av4: ")) #Variável criada anteriomente para a leitura dos valores
av5 = float(input("Digite o Valor da Av5: ")) #Variável criada anteriomente para a leitura dos valores
media = calculo_media(av1, av2, av3, av4, av5) #Chamada da função para calcular a média e retornar com o resultado
print(media)