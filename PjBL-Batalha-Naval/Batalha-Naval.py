import random
import time
import pygame

#LEMBRE-SE DE INSTALAR A BIBLIOTECA PYGAME!!!! (pip install pygame-ce)


def artes(escolha):
    batalha_naval = r'''
        _________         __         .__  .__                _______                      .__   
        \______  \_____ _/  |______  |  | |  |__ _____       \      \ _____ ___  _______  |  |  
        |    |  _/\__  \\   __\__  \ |  | |  |  \\__  \      /   |   \\__  \\  \/ /\__  \ |  |  
        |    |   \ / __ \|  |  / __ \|  |_|   Y  \/ __ \_   /    |    \/ __ \\   /  / __ \|  |__
        |______  /(____  /__| (____  /____/___|  (____  /   \____|__  (____  /\_/  (____  /____/
               \/      \/          \/          \/     \/            \/     \/           \/      
    '''
    wave = r'''
          ~~~~~~~~~~~                ~~~~~~~~~~~                ~~~~~~~~~~~                ~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~          ~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~~~~        ~~~~~~~~~~~~~~~~~~~    
~~~~~~~~~~           ~~~~~~~~~~~~~~~~           ~~~~~~~~~~~~~~~~           ~~~~~~~~~~~~~~~~           ~~~~   
~~~~~~                   ~~~~~~~~                   ~~~~~~~~                   ~~~~~~~~                   
    '''
    introducao = r'''                                         VAMOS COMEÇAR?
                  Mas antes, você deve posicionar seus barcos no tabuleiro!'''
    inicio_da_batalha = "AGORA SIM A BATALHA COMEÇOU!\n\nQuem afundar todos os barcos do oponente primeiro ganha!"
    separacao = "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    if escolha == 1:
        return batalha_naval
    elif escolha == 2:
        return wave
    elif escolha == 3:
        return introducao
    elif escolha == 4:
        return inicio_da_batalha
    elif escolha == 5:
        return separacao
    
def musica_fundo():
    pygame.init()
    pygame.mixer.music.load("soundtrack.mp3")
    pygame.mixer.music.play(-1)

def som_afundar():
    som = pygame.mixer.Sound("som_afundar.mp3")
    som.play()

def som_errar():
    som = pygame.mixer.Sound("som_errar.mp3")
    som.play()
    

def tabuleiro_computador():
    matriz = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    quantidade = 0

    # Preenchimento da matriz com números aleatórios com verificação se a posição já está preenchida ou não
    while quantidade < 5:
        linha = random.randint(0,4)
        coluna = random.randint(0,9)

        if matriz[linha][coluna] != 'N':
            matriz[linha][coluna] = 'N'
            quantidade += 1
    
    return matriz

def tabuleiro_computador_feedback():
    # Criação da matriz de feedback vazia
    matriz = [
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
    ]

    return matriz

        
def tabuleiro_jogador():
    matriz = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
    ]

    quantidade = 0

    # Preenchimento da matriz com as posições desejadas pelo jogador com verificação de preenchimento da matriz
    while quantidade < 5:
        # Impressão da matriz atual
        print("\nSEU TABULEIRO ATUALMENTE: \n")
        for i in range(5):
            print(matriz[i])

        # Input da linha que o usuário deseja colocar o navio
        print(" ")
        linha = input("Escolha a linha que você quer posicionar seu navio (0-4): ")
        while not linha.isdigit() or int(linha) > 4 or int(linha) < 0:
            print("Digite valores válidos!")
            linha = input("Escolha a linha que você quer posicionar o seu navio (0-4): ")
        
        # Input da coluna que o usuário deseja colocar o navio
        coluna = input("Escolha a coluna que você quer posicionar seu navio (0-9): ")
        while not coluna.isdigit()  or int(coluna) > 9 or int(coluna) < 0:
            print("Digite valores válidos!")
            coluna = input("Escolha a coluna que você quer posicionar seu navio (0-9): ")

        # Conversão dos valores dos input's para int (fizemos isso para poder utilizar a função .isdigit() e somente receber números como input)
        linha = int(linha)
        coluna = int(coluna)

        # Se a posição já tiver um barco a quantidade não é acrescida e o loop é repetido até que quantidade seja igual a 5
        if matriz[linha][coluna] != 'N':
            matriz[linha][coluna] = 'N'
            quantidade += 1
        else: 
            print("Posição já ocupada! Digite outra posição!")
    
    # Impressão do tabuleiro ao final do preenchimento do usuário
    time.sleep(1)
    print("\nSEU TABULEIRO FICOU ASSIM: \n")
    for i in range(5):
        print(matriz[i])
    
    return matriz

def tabuleiro_jogador_feedback():
    # Criação da matriz de feedback vazia
    matriz = [
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
        ['~','~','~','~','~','~','~','~','~','~'],
    ]

    return matriz

def ataque_computador(matriz, feedback):
    time.sleep(1)
    print("Ataque do Computador!\n")
    time.sleep(1)
    linha_atacada = random.randint(0,4)
    coluna_atacada = random.randint(0,9)

    # Os valores de linha e coluna atacada são randomizados até que a posição não seja uma posição atacada para evitar ataques repetidos
    while feedback[linha_atacada][coluna_atacada] == 'X' or feedback[linha_atacada][coluna_atacada] == 'O':
        linha_atacada = random.randint(0,4)
        coluna_atacada = random.randint(0,9)
    
    # for i in range(1,4):
    #     print(i)
    #     time.sleep(0.5)
    #     if i == 3:
    #         print("\nJÁ\n")
    #         time.sleep(1)

    # Impressão do tabuleiro com o navio atacado
    if matriz[linha_atacada][coluna_atacada] == 'N':
        feedback[linha_atacada][coluna_atacada] = 'X'
        som_afundar()
        print("COMPUTADOR ACERTOU!")
        time.sleep(1)
        print("\nTabuleiro atual do Jogador:\n")
        time.sleep(1)
        for i in range(5):
            print(feedback[i])
    # Impressão do tabuleiro ao errar o navio
    else:
        feedback[linha_atacada][coluna_atacada] = 'O'
        som_errar()
        print("COMPUTADOR ERROU!")
        time.sleep(1)
        print("\nTabuleiro atual do Jogador:\n")
        time.sleep(1)
        for i in range(5):
            print(feedback[i])

    # Cada 'X' representa uma embarcação atingida, então os 'X''s são contados e subtraídos de 5 para mostrar quantas embarcações restam no tabuleiro
    embarcacoes_atingidas = sum(linha.count('X') for linha in feedback)
    time.sleep(1)
    print("\nRestam ", 5-embarcacoes_atingidas," embarcações!")

    return feedback

def ataque_jogador(matriz, feedback):
    time.sleep(1)
    print(artes(5))
    time.sleep(1)
    print("Ataque do Jogador!\n")
    time.sleep(1)

    # Input de qual linha o usuário quer atacar e verificação se é um valor válido
    linha_atacada = input("Linha onde deseja bombardear (0-4): ")
    while not linha_atacada.isdigit() or int(linha_atacada) > 4 or int(linha_atacada) < 0:
        print("Digite valores válidos!")
        linha_atacada = input("Linha onde deseja bombardear (0-4): ")
    
    # Input de qual coluna o usuário quer atacar e verificação se é um valor válido
    coluna_atacada = input("Coluna onde deseja bombardear (0-9): ")
    while not coluna_atacada.isdigit() or int(coluna_atacada) > 9 or int(coluna_atacada) < 0:
        print("Digite valores válidos!")
        coluna_atacada = input("Coluna onde deseja bombardear (0-9): ")
    
    # Conversão dos valores dos input's para int (fizemos isso para poder utilizar a função .isdigit() e somente receber números como input)
    linha_atacada = int(linha_atacada)
    coluna_atacada = int(coluna_atacada)

    # Verificação se a coordenada já foi atacada
    while feedback[linha_atacada][coluna_atacada] == 'X' or feedback[linha_atacada][coluna_atacada] == 'O':
        print("Esta coordenada já foi atacada!")

        # Input de qual linha o usuário quer atacar e verificação se é um valor válido
        linha_atacada = input("Linha onde deseja bombardear (0-4): ")
        while not linha_atacada.isdigit() or int(linha_atacada) > 4 or int(linha_atacada) < 0:
            print("Digite valores válidos!")
            linha_atacada = input("Linha onde deseja bombardear (0-4): ")

        # Input de qual linha o usuário quer atacar e verificação se é um valor válido
        coluna_atacada = input("Coluna onde deseja bombardear (0-9): ")
        while not coluna_atacada.isdigit() or int(coluna_atacada) > 9 or int(coluna_atacada) < 0:
            print("Digite valores válidos!")
            coluna_atacada = input("Coluna onde deseja bombardear (0-9): ")

        # Conversão dos valores dos input's para int (fizemos isso para poder utilizar a função .isdigit() e somente receber números como input)
        linha_atacada = int(linha_atacada)
        coluna_atacada = int(coluna_atacada)

    # Impressão do tabuleiro com o navio atacado   
    if matriz[linha_atacada][coluna_atacada] == 'N':
        feedback[linha_atacada][coluna_atacada] = 'X'
        time.sleep(1)
        som_afundar()
        print("\nJOGADOR ACERTOU!")
        time.sleep(1)
        print("\nTabuleiro atual do Computador:\n")
        time.sleep(1)
        for i in range(5):
            print(feedback[i])
    # Impressão do tabuleiro ao errar o navio
    else:
        feedback[linha_atacada][coluna_atacada] = 'O'
        time.sleep(1)
        som_errar()
        print("\nJOGADOR ERROU!")
        time.sleep(1)
        print("\nTabuleiro atual do Computador:\n")
        time.sleep(1)
        for i in range(5):
            print(feedback[i])

    # Cada 'X' representa uma embarcação atingida, então os 'X''s são contados e subtraídos de 5 para mostrar quantas embarcações restam no tabuleiro
    embarcacoes_atingidas = sum(linha.count('X') for linha in feedback)
    time.sleep(1)
    print("\nRestam ", 5-embarcacoes_atingidas," embarcações!")
        
    return feedback

def navios_afundados(feedback):
    quantidade_navios_afundados = 0
    for i in feedback:
        quantidade_navios_afundados += i.count('X')

    return quantidade_navios_afundados
    
def main():
    musica_fundo()
    rodada_atual = 0
    print(artes(1))
    print(artes(2))
    time.sleep(1)
    print(artes(3))
    time.sleep(1)
    matriz_computador = tabuleiro_computador()
    feedback_computador = tabuleiro_computador_feedback()
    matriz_jogador = tabuleiro_jogador()
    feedback_jogador = tabuleiro_jogador_feedback()
    time.sleep(1)
    print(artes(5))
    time.sleep(1)
    print(artes(4))
    time.sleep(1)
    # Loop até que 5 'X''s sejam contados em alguma das matrizes de feedback
    while navios_afundados(feedback_computador) < 5 and navios_afundados(feedback_jogador) < 5:
        print(artes(5))
        time.sleep(1)
        rodada_atual += 1
        print(f"RODADA {rodada_atual}")
        time.sleep(1)
        print(artes(5))
        feedback_jogador = ataque_computador(matriz_jogador,feedback_jogador)
        # Break para garantir que ao ganhar o jogo pare instantaneamente
        if sum(linha.count('X') for linha in feedback_jogador) == 5:
            break

        feedback_computador = ataque_jogador(matriz_computador,feedback_computador)

        if sum(linha.count('X') for linha in feedback_computador) == 5:
            break

    # Impressão do vencedor
    if navios_afundados(feedback_computador) == 5:
        print(artes(5))
        print("Vitória do Jogador!")
    elif navios_afundados(feedback_jogador) == 5:
        print(artes(5))
        print("Vitória do Computador!")
    
    print("Muito obrigado por jogar! Jogo desenvolvido por: Guilherme Martins Muniz, Gustavo Kenzo Sato Hamada e Pedro Joaquim Freire de Lima")
    print("========================================\n")
    pygame.mixer.music.stop()

main()