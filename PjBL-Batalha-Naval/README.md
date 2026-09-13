**Batalha Naval em Python**

**Autores**

Guilherme Martins Muniz

Gustavo Kenzo Sato Hamada

Pedro Joaquim Freire de Lima

**Descrição do Projeto**

Este projeto consiste na implementação do jogo Batalha Naval utilizando a linguagem Python. O sistema permite que um jogador dispute uma partida contra o computador, posicionando embarcações em um tabuleiro e realizando ataques alternados até que todos os navios de um dos participantes sejam destruídos.

O projeto foi desenvolvido com foco na aplicação de conceitos fundamentais de programação, incluindo estruturas de repetição, estruturas condicionais, matrizes, funções, validação de entradas, geração de números aleatórios e modularização do código.

Além disso, foi utilizada a biblioteca Pygame para a reprodução de efeitos sonoros e música de fundo durante a execução do jogo.

**Objetivos**

Aplicar conceitos de lógica de programação.

Utilizar matrizes para representação de tabuleiros.

Implementar interação entre usuário e sistema.

Desenvolver validação de dados de entrada.

Utilizar bibliotecas externas para aprimorar a experiência do usuário.

Criar uma estrutura de código organizada por funções.

**Tecnologias Utilizadas**

Python 3

Pygame

Random

Time

**Funcionamento do Sistema**

Inicialização

Ao iniciar o programa, são exibidas mensagens introdutórias e reproduzida uma trilha sonora de fundo.

Em seguida, são criados:

O tabuleiro do computador;

O tabuleiro do jogador;

Os tabuleiros de feedback utilizados para registrar os ataques realizados durante a partida.

**Posicionamento dos Navios**

O computador posiciona automaticamente cinco embarcações em coordenadas aleatórias do tabuleiro.

O jogador escolhe manualmente as coordenadas para posicionar suas cinco embarcações. O sistema valida as entradas e impede que dois navios ocupem a mesma posição

**Sistema de Ataques**

A partida ocorre em rodadas.

Em cada rodada:

O computador realiza um ataque aleatório ao tabuleiro do jogador.

O jogador escolhe uma coordenada para atacar o tabuleiro do computador.

O sistema verifica se houve acerto ou erro.

O tabuleiro de feedback é atualizado.

É exibida a quantidade de embarcações restantes.

O sistema também impede que uma posição seja atacada mais de uma vez.

**Condição de Vitória**

A partida é encerrada quando um dos participantes alcança cinco acertos, correspondentes à destruição de todas as embarcações adversárias.

**Estrutura do Código**

<img width="885" height="284" alt="image" src="https://github.com/user-attachments/assets/346236e1-caa0-4e5a-8420-200e03e1796e" />

**Função artes()**

Responsável por armazenar e retornar os elementos visuais em ASCII utilizados durante a execução do jogo, incluindo:

Título do jogo;

Elementos decorativos;

Mensagens de introdução;

Separadores visuais.

--------------------------------------------------------------------------------------------------------------------------------

<img width="449" height="79" alt="image" src="https://github.com/user-attachments/assets/1c67d27b-a055-42d6-a4af-e63585c2b7c1" />

**Função musica_fundo()**

Inicializa a biblioteca Pygame e reproduz a trilha sonora principal em modo contínuo.

--------------------------------------------------------------------------------------------------------------------------------

<img width="466" height="56" alt="image" src="https://github.com/user-attachments/assets/125d530d-bb66-4bc8-89f0-90ee595c3d81" />

**Função som_afundar()**

Executa o efeito sonoro associado a um ataque bem-sucedido.

--------------------------------------------------------------------------------------------------------------------------------

<img width="435" height="61" alt="image" src="https://github.com/user-attachments/assets/bb715e1e-c3f6-4143-a843-887b8b1a633e" />

**Função som_errar()**

Executa o efeito sonoro associado a um ataque sem sucesso.

--------------------------------------------------------------------------------------------------------------------------------

<img width="909" height="405" alt="image" src="https://github.com/user-attachments/assets/8a6745fb-627a-4012-ac49-7ae5356d554d" />

**Função tabuleiro_computador()**

Cria e preenche automaticamente o tabuleiro do computador com cinco embarcações posicionadas aleatoriamente.

--------------------------------------------------------------------------------------------------------------------------------

<img width="496" height="213" alt="image" src="https://github.com/user-attachments/assets/62599cc1-3b4c-45d2-8a20-3eb5c2f44f68" />

**Função tabuleiro_computador_feedback()**

Cria o tabuleiro utilizado pelo jogador para acompanhar os resultados de seus ataques.

--------------------------------------------------------------------------------------------------------------------------------

<img width="1138" height="884" alt="image" src="https://github.com/user-attachments/assets/7a3b3f63-3b79-4084-b7cb-edd235120788" />

**Função ataque_computador()**

Controla os ataques realizados pelo computador, verificando acertos, erros e ataques repetidos.

--------------------------------------------------------------------------------------------------------------------------------

<img width="1146" height="812" alt="image" src="https://github.com/user-attachments/assets/77dbf93c-5da3-47f9-a097-9978f6518e8c" />
<img width="1148" height="534" alt="image" src="https://github.com/user-attachments/assets/ef814e77-317c-41f4-b013-31e0130157e0" />

**Função ataque_jogador()**

Recebe as coordenadas informadas pelo jogador, valida os dados e atualiza o tabuleiro de acordo com o resultado do ataque.

--------------------------------------------------------------------------------------------------------------------------------

<img width="561" height="113" alt="image" src="https://github.com/user-attachments/assets/c874b8cc-75e7-4b68-a8b6-4e691960a671" />

**Função navios_afundados()**

Calcula a quantidade de embarcações atingidas em um determinado tabuleiro de feedback.

--------------------------------------------------------------------------------------------------------------------------------

<img width="1144" height="898" alt="image" src="https://github.com/user-attachments/assets/57d477dc-1f2c-4d23-aa22-4b2be44c69ea" />

**Função main()**

Função principal do programa. Coordena todas as etapas do jogo, incluindo:

Inicialização dos recursos;

Criação dos tabuleiros;

Controle das rodadas;

Verificação das condições de vitória;

Encerramento da aplicação.

--------------------------------------------------------------------------------------------------------------------------------

**Instalação e Execução**

**Pré-requisitos**

Python 3 instalado.

Biblioteca Pygame instalada.

Instalação da biblioteca:

pip install pygame-ce

**Arquivos Necessários**

Os seguintes arquivos devem estar localizados no mesmo diretório do programa:

soundtrack.mp3

som_afundar.mp3

som_errar.mp3

**Execução**

Execute o arquivo principal utilizando o comando:

python batalha_naval.py

**Considerações Finais**

O desenvolvimento deste projeto permitiu a aplicação prática dos conceitos estudados durante a disciplina, contribuindo para o aprimoramento das habilidades relacionadas à programação estruturada, manipulação de matrizes, organização de código e resolução de problemas computacionais.
