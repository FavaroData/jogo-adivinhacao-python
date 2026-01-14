Jogo de Adivinhação com Feedback Inteligente

Projeto em Python que implementa um jogo de adivinhação baseado em lógica de aproximação numérica.  
O programa escolhe um número aleatório entre 1 e 100, e o jogador tenta acertá-lo no menor número de tentativas possível.
A lógica aplicada consiste no algorítimo binário, no qual implica uma estratégia que encontra um valor em um conjunto ordenado dividindo o intervalo de busca pela metade a cada tentativa, eliminando rapidamente grandes partes da sequência até localizar o valor desejado.

## Como funciona:
A cada tentativa, o jogo fornece dicas baseadas na distância entre o chute e o número correto:

- **Muito Baixo** → mais de 10 números abaixo
- **Baixo** → entre 1 e 10 números abaixo
- **Alto** → entre 1 e 10 números acima
- **Muito Alto** → mais de 10 números acima
- **Muito perto** → diferença de apenas 1 número

## Tecnologias utilizadas
- Python 3
- Biblioteca `random` (para randomizar um número dentro de um range de 1, 100)
- Biblioteca `os` (para limpar o terminal)

