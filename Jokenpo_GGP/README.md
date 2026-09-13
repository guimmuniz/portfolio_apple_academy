**Jokenpô em Python**

Este projeto tem como objetivo implementar o jogo Jokenpô (Pedra, Papel e Tesoura) em Python, utilizando interação via terminal. O programa oferece múltiplas modalidades de jogo e utiliza animações em ASCII para tornar a execução mais dinâmica.

**Como executar o projeto**

Siga os passos abaixo para rodar o jogo corretamente:

1. Instale o Python

Certifique-se de que o Python está instalado em seu computador (não apenas no VS Code).

Download oficial: https://www.python.org/downloads/

Durante a instalação, marque a opção "Add Python to PATH"

2. Instale a biblioteca necessária

Abra o terminal (Prompt de Comando ou terminal do VS Code) e execute:

python -m pip install pwinput

Agora seu computador está apto a executar nosso projeto!

**Regras do Jogo**

O sistema segue as regras tradicionais:

Pedra vence Tesoura

Tesoura vence Papel

Papel vence Pedra

Escolhas iguais resultam em empate

**Estrutura Geral do Programa**

O programa é dividido em três etapas principais:

Escolha da modalidade

Execução das rodadas

Encerramento e exibição do placar

**Inicialização**

Ao iniciar, o sistema apresenta as modalidades disponíveis:

<img width="580" height="336" alt="image" src="https://github.com/user-attachments/assets/dbf48d67-df64-4ffa-960e-ce2ed0b0ad67" />


O valor digitado é validado para garantir que esteja entre 1 e 3. Caso contrário, o programa solicita uma nova entrada.

O jogo é executado dentro de um laço de repetição (while infinito != 0), permitindo múltiplas rodadas até que o usuário escolha encerrar.

**Lógica de Cada Modalidade**

**1. Jogador vs Jogador**

O Jogador 1 escolhe sua jogada

O Jogador 2 escolhe sua jogada

Ambas as entradas são validadas

O sistema compara os valores
<img width="1090" height="694" alt="image" src="https://github.com/user-attachments/assets/65cf1f3b-2283-443a-824e-63e208d1ffcd" />

Após isso, o programa executa a animação:

3...

2...

1...

JÁ!

E revela o resultado:

ESCOLHA JOGADOR UM: PEDRA

VS

ESCOLHA JOGADOR DOIS: TESOURA

JOGADOR UM venceu!

**2. Jogador vs Computador**

O jogador escolhe sua jogada

O computador gera um número aleatório (random.randint(1,3))

O sistema compara as escolhas

<img width="633" height="397" alt="image" src="https://github.com/user-attachments/assets/7ce82c67-0fe1-41bf-b750-30cabf09bedb" />

**Lógica de Decisão (Jogador vs Computador)**

O trecho abaixo é responsável por determinar o resultado da rodada na modalidade Jogador vs Computador, comparando a escolha do usuário com a escolha gerada aleatoriamente pelo computador.

<img width="515" height="504" alt="image" src="https://github.com/user-attachments/assets/5d1cc656-f57b-4edf-97bb-ac35c72ff2be" />


<img width="558" height="912" alt="image" src="https://github.com/user-attachments/assets/10e140d1-7927-4d8f-880e-3b3659331202" />


Nesta parte abaixo mostra se o jogador quer continuar ou encerrar o programa

digite 1 para continuar

digite 2 para encerrar o programa


<img width="410" height="144" alt="image" src="https://github.com/user-attachments/assets/172049af-a152-48e6-917d-da48fcbc439a" />


**3. Computador vs Computador**

Ambos os jogadores são simulados

Cada computador gera sua jogada aleatoriamente

O resultado é exibido automaticamente

<img width="621" height="720" alt="image" src="https://github.com/user-attachments/assets/4174723a-fb32-4d90-9fe1-67d9dd38d23c" />

**Lógica de Decisão (Computador vs Computador)**

Este trecho do código é responsável por determinar o resultado da rodada na modalidade Computador vs Computador, onde ambas as jogadas são geradas automaticamente.

<img width="493" height="844" alt="image" src="https://github.com/user-attachments/assets/1acfa48c-3d11-4878-8c58-98dd153a62ef" />
<img width="491" height="572" alt="image" src="https://github.com/user-attachments/assets/9f3d1ed8-1e10-463a-b754-7a71c3cb6e3c" />

Nesta parte abaixo mostra se o jogador quer continuar ou encerrar o programa

digite 1 para continuar

digite 2 para encerrar o programa


<img width="485" height="122" alt="image" src="https://github.com/user-attachments/assets/12f47878-b03a-4deb-80ac-75fb9de1d64e" />

Após terminar, ele mostra o placar do jogo

**Placar do Humano x Humano**

<img width="787" height="161" alt="image" src="https://github.com/user-attachments/assets/04802ada-1d2f-4a1b-be61-2c7b2a495c50" />


**Placar Humano x Computador**

<img width="722" height="158" alt="image" src="https://github.com/user-attachments/assets/21c7684c-2e62-4df6-b8fa-8076784e62f2" />


**Placar Computador x Computador**

<img width="901" height="158" alt="image" src="https://github.com/user-attachments/assets/e7f0a504-f248-436c-8f98-dfd07ee1dd53" />










