Jogo de Adivinhação com Feedback Inteligente

Projeto em Python que implementa um jogo de adivinhação baseado em lógica de aproximação numérica.  
A lógica aplicada consiste no algorítimo binário, no qual implica uma estratégia que encontra um valor em um conjunto ordenado dividindo o intervalo de busca pela metade a cada tentativa, eliminando rapidamente grandes partes da sequência até localizar o valor desejado.

## Como funciona:

• No modo_jogador:
O programa escolhe um número aleatório entre 1 e 100, e o jogador tenta acertá-lo no menor número de tentativas possível.

• No modo_computador:
Você decide um número, e o computador tenta acertar que número é este baseando-se nas suas respostas.

O jogo utiliza dicas baseadas na distância entre o chute e o número correto:

- **Muito Baixo** → mais de 10 números abaixo
- **Baixo** → entre 1 e 10 números abaixo
- **Alto** → entre 1 e 10 números acima
- **Muito Alto** → mais de 10 números acima
- **Muito perto** → diferença de apenas 1 número

## Tecnologias utilizadas
- Python 3

## Conceitos praticados
- Lógica de programação
- Funções
- Modularização de código
- Manipulação de entrada do usuário
- Condicionais (`if / elif / else`)
- Importação de módulos
- Uso de bibliotecas(`os` e `random`)
- Estruturas de repetição
- Validação de entrada
