import random
import time
import pwinput

infinito = 1
placarHumano = 0
placarMaquina = 0
placarJogadorUm = 0
placarJogadorDois = 0
placarComputadorUm = 0
placarComputadorDois = 0

maoTres = '''
  ____    ___
 |    -  |   -  ---
 |     | |    ||    -
  |    | |    |     |   
  #    ||    |     |
 |     ||    |    |--
|---------   |  |   |
|    ____-      |   )
 |       |      |___) 
  #       |      ==
   #_  __|     ===
     ===========
'''

maoDois = '''
  ____    ___
 |    -  |   -  
 |     | |    |   
  |    | |    |        
  #    ||    |     
 |     ||   _|_  ___
|--------- |   ||   |
|    ____- |   ||   )
 |       | |___)|___) 
  #       |      ==
   #_  __|     ===
     ===========
'''

maoUm = '''
  ____   
 |    - 
 |     |  
  |    |      
  #    |     
 |     |-- -__  ___
|---------||   ||   |
|    ____-||   ||   )
 |       |||___)|___) 
  #       |      ==
   #_  __|     ===
     ===========
'''

jokenpo = '''
       __   ____     __ __    ______    _   __    ____    ____
      / /  / __ |   / //_/   / ____/   / | / /   / __ |  / __ |
 __  / /  / / / /  / ,<     / __/     /  |/ /   / /_/ / / / / /
/ /_/ /  / /_/ /  / /| |   / /___    / /|  /   / ____/ / /_/ /
|____/   |____/  /_/ |_|  /_____/   /_/ |_/   /_/      |____/
'''

divisao = '''==============================================================='''

ja = '''
       __    ___     __
      / /   /   |   / /
 __  / /   / /| |  / /
/ /_/ /   / ___ | /_/
|____/   /_/  |_|(_)
'''

pedra = '''
    _____
---'__   |__
      |  |__)
      |__)__)
      (_____)
---.__(____)
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

vs = '''
 _    __   _____
| |  / /  / ___/
| | / /   |__  |
| |/ /   ___/ /
|___/   /____/
'''

placar = '''
    ____     __     ___    ______    ___     ____
   / __ |   / /    /   |  / ____/   /   |   / __ |
  / /_/ /  / /    / /| | / /       / /| |  / /_/ /
 / ____/  / /___ / ___ |/ /___    / ___ | / _, _/
/_/      /_____//_/  |_||____/   /_/  |_|/_/ |_|
'''

print(jokenpo)
print(divisao)
print("MODALIDADES")
print(" ")
print("Jogador VS Jogador - 1")
print(" ")
print("Jogador VS Computador - 2")
print(" ")
print("Computador VS Computador - 3")
print(" ")
escolhaModalidade = int(input("Escolha a modalidade: "))

while escolhaModalidade < 1 or escolhaModalidade > 3:
        print(" ")
        print("Escolha um número entre 1 e 3!")
        print(" ")
        escolhaModalidade = int(input("Digite novamente sua escolha: "))

if(escolhaModalidade == 1):
    while infinito != 0:
        print(divisao)
        print("ESCOLHA SUA JOGADA - JOGADOR 1")
        print(" ")
        print("Pedra - 1")
        print(" ")
        print("Papel - 2")
        print(" ")
        print("Tesoura - 3")
        print(" ")
        escolhaJogadorUm = int(pwinput.pwinput(prompt='Digite sua escolha: ', mask='*'))

        while escolhaJogadorUm < 1 or escolhaJogadorUm > 3:
            print(" ")
            print("Escolha um numero entre 1 e 3!")
            print(" ")
            escolhaJogadorUm = int(pwinput.pwinput(prompt='Digite novamente sua escolha: ', mask='*'))
        
        print(divisao)

        print("ESCOLHA SUA JOGADA - JOGADOR 2")
        print(" ")
        print("Pedra - 1")
        print(" ")
        print("Papel - 2")
        print(" ")
        print("Tesoura - 3")
        print(" ")
        escolhaJogadorDois = int(pwinput.pwinput(prompt='Digite sua escolha: ', mask='*'))

        while escolhaJogadorDois < 1 or escolhaJogadorDois > 3:
            print(" ")
            print("Escolha um numero entre 1 e 3!")
            print(" ")
            escolhaJogadorDois = int(pwinput.pwinput(prompt='Digite novamente sua escolha: ', mask='*'))

        print(divisao)
        time.sleep(1)
        print(" ")
        print(maoTres)
        time.sleep(1)
        print(" ")
        print(maoDois)
        time.sleep(1)
        print(" ")
        print(maoUm)
        time.sleep(1)
        print(" ")
        print(ja)
        time.sleep(1)
        print(" ")
        print(divisao)

        if(escolhaJogadorUm == 1):
            print("ESCOLHA JOGADOR UM:")
            time.sleep(1)
            print(pedra)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA JOGADOR DOIS:")
            time.sleep(1)
            if(escolhaJogadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(escolhaJogadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("JOGADOR DOIS venceu!")
                placarJogadorDois+= 1
            elif(escolhaJogadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("JOGADOR UM venceu!")
                placarJogadorUm+= 1

        elif(escolhaJogadorUm == 2):
            print("ESCOLHA JOGADOR UM:")
            time.sleep(1)
            print(papel)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA JOGADOR DOIS:")
            time.sleep(1)
            if(escolhaJogadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("JOGADOR UM venceu!")
                placarJogadorUm+= 1
            elif(escolhaJogadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(escolhaJogadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("JOGADOR DOIS venceu!")
                placarJogadorDois+= 1

        elif(escolhaJogadorUm == 3):
            print("ESCOLHA JOGADOR UM:")
            time.sleep(1)
            print(tesoura)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA JOGADOR DOIS:")
            time.sleep(1)
            if(escolhaJogadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("JOGADOR DOIS venceu!")
                placarJogadorDois+= 1
            elif(escolhaJogadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("JOGADOR UM venceu!")
                placarJogadorUm+= 1
            elif(escolhaJogadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("Empate!")
        
        print(divisao)
        print("Continuar - 1")
        print(" ")
        print("Sair - 0")
        print(" ")
        escolhaContinuar = int(input("Sua escolha: "))

        while escolhaContinuar < 0 or escolhaContinuar > 1:
          print(" ")
          print("Escolha um número entre 0 e 1!")
          print(" ")
          escolhaContinuar = int(input("Digite novamente sua escolha: "))
        
        if(escolhaContinuar == 0):
            print(divisao)
            time.sleep(1)
            print(placar)
            time.sleep(1)
            print(" ")
            print(f"JOGADOR UM - {placarJogadorUm} X JOGADOR DOIS - {placarJogadorDois}")
            print(" ")
            infinito = 0
            print("OBRIGADO POR JOGAR! JOGO FEITO POR: GUILHERME MARTINS MUNIZ, GUSTAVO KENZO SATO HAMADA E PEDRO JOAQUIM FREIRE DE LIMA")
            print(" ")

elif(escolhaModalidade == 2):
    while infinito != 0:
        print(divisao)
        print("ESCOLHA SUA JOGADA")
        print(" ")
        print("Pedra - 1")
        print(" ")
        print("Papel - 2")
        print(" ")
        print("Tesoura - 3")
        print(" ")
        escolha = int(input("Digite sua escolha: "))

        while escolha < 1 or escolha > 3:
            print(" ")
            print("Escolha um numero entre 1 e 3!")
            print(" ")
            escolha = int(input("Digite novamente sua escolha: "))

        numeroAleatorio = random.randint(1, 3)

        print(divisao)
        time.sleep(1)
        print(" ")
        print(maoTres)
        time.sleep(1)
        print(" ")
        print(maoDois)
        time.sleep(1)
        print(" ")
        print(maoUm)
        time.sleep(1)
        print(" ")
        print(ja)
        time.sleep(1)
        print(" ")
        print(divisao)

        if(escolha == 1):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(pedra)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if (numeroAleatorio == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(numeroAleatorio == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1

        elif(escolha == 2):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(papel)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if(numeroAleatorio == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1
            elif (numeroAleatorio == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(numeroAleatorio == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1

        elif(escolha == 3):
            print("SUA ESCOLHA:")
            time.sleep(1)
            print(tesoura)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA DO COMPUTADOR:")
            time.sleep(1)
            if(numeroAleatorio == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR venceu!")
                placarMaquina+= 1
            elif(numeroAleatorio == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("HUMANO venceu!")
                placarHumano+= 1
            elif (numeroAleatorio == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("Empate!")
        
        print(divisao)
        print("Continuar - 1")
        print(" ")
        print("Sair - 0")
        print(" ")
        escolhaContinuar = int(input("Sua escolha: "))

        while escolhaContinuar < 0 or escolhaContinuar > 1:
          print(" ")
          print("Escolha um número entre 0 e 1!")
          print(" ")
          escolhaContinuar = int(input("Digite novamente sua escolha: "))
        
        if(escolhaContinuar == 0):
            print(divisao)
            time.sleep(1)
            print(placar)
            time.sleep(1)
            print(" ")
            print(f"HUMANO - {placarHumano} X COMPUTADOR - {placarMaquina}")
            print(" ")
            infinito = 0
            print("OBRIGADO POR JOGAR! JOGO FEITO POR: GUILHERME MARTINS MUNIZ, GUSTAVO KENZO SATO HAMADA E PEDRO JOAQUIM FREIRE DE LIMA")
            print(" ")

elif(escolhaModalidade == 3):
    while infinito != 0:
        print(divisao)
        print("COMPUTADOR 1 ESTÁ ESCOLHENDO UM ENTRE ESSES")
        print(" ")
        time.sleep(0.5)
        print("Pedra - 1")
        print(" ")
        time.sleep(0.5)
        print("Papel - 2")
        print(" ")
        time.sleep(0.5)
        print("Tesoura - 3")
        print(" ")
        time.sleep(2)
        
        escolhaComputadorUm = random.randint(1, 3)

        print("COMPUTADOR 1 FEZ SUA ESCOLHA")
        print(divisao)
        time.sleep(0.5)

        print("COMPUTADOR 2 ESTÁ ESCOLHENDO UM ENTRE ESSES")
        print(" ")
        time.sleep(0.5)
        print("Pedra - 1")
        print(" ")
        time.sleep(0.5)
        print("Papel - 2")
        print(" ")
        time.sleep(0.5)
        print("Tesoura - 3")
        print(" ")
        time.sleep(2)

        escolhaComputadorDois = random.randint(1, 3)
        print("COMPUTADOR 2 FEZ SUA ESCOLHA")

        print(divisao)
        time.sleep(1)
        print(" ")
        print(maoTres)
        time.sleep(1)
        print(" ")
        print(maoDois)
        time.sleep(1)
        print(" ")
        print(maoUm)
        time.sleep(1)
        print(" ")
        print(ja)
        time.sleep(1)
        print(" ")
        print(divisao)

        if(escolhaComputadorUm == 1):
            print("ESCOLHA COMPUTADOR UM:")
            time.sleep(1)
            print(pedra)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA COMPUTADOR DOIS:")
            time.sleep(1)
            if (escolhaComputadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(escolhaComputadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR DOIS venceu!")
                placarComputadorDois+= 1
            elif(escolhaComputadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR UM venceu!")
                placarComputadorUm+= 1

        elif(escolhaComputadorUm == 2):
            print("ESCOLHA COMPUTADOR UM:")
            time.sleep(1)
            print(papel)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA COMPUTADOR DOIS:")
            time.sleep(1)
            if(escolhaComputadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR UM venceu!")
                placarComputadorUm+= 1
            elif (escolhaComputadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("Empate!")
            elif(escolhaComputadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR DOIS venceu!")
                placarComputadorDois+= 1

        elif(escolhaComputadorUm == 3):
            print("ESCOLHA COMPUTADOR UM:")
            time.sleep(1)
            print(tesoura)
            print(" ")
            time.sleep(1)
            print(vs)
            time.sleep(1)
            print(" ")
            print("ESCOLHA COMPUTADOR DOIS:")
            time.sleep(1)
            if(escolhaComputadorDois == 1):
                print(pedra)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR DOIS venceu!")
                placarComputadorDois+= 1
            elif(escolhaComputadorDois == 2):
                print(papel)
                time.sleep(2)
                print(divisao)
                print("COMPUTADOR UM venceu!")
                placarComputadorUm+= 1
            elif (escolhaComputadorDois == 3):
                print(tesoura)
                time.sleep(2)
                print(divisao)
                print("Empate!")
        
        print(divisao)
        print("Continuar - 1")
        print(" ")
        print("Sair - 0")
        print(" ")
        escolhaContinuar = int(input("Sua escolha: "))

        while escolhaContinuar < 0 or escolhaContinuar > 1:
          print(" ")
          print("Escolha um número entre 0 e 1!")
          print(" ")
          escolhaContinuar = int(input("Digite novamente sua escolha: "))
        
        if(escolhaContinuar == 0):
            print(divisao)
            time.sleep(1)
            print(placar)
            time.sleep(1)
            print(" ")
            print(f"COMPUTADOR UM - {placarComputadorUm} X COMPUTADOR DOIS - {placarComputadorDois}")
            print(" ")
            infinito = 0
            print("OBRIGADO POR JOGAR! JOGO FEITO POR: GUILHERME MARTINS MUNIZ, GUSTAVO KENZO SATO HAMADA E PEDRO JOAQUIM FREIRE DE LIMA")
            print(" ")
