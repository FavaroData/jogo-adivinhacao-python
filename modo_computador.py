import os

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def calcular_chute(minimo, maximo):
    return (minimo + maximo) // 2


def validar_resposta(resposta):
    respostas_validas = ['alto', 'baixo', 'muito alto', 'muito baixo', 'sim']
    return resposta in respostas_validas

def jogar():

    limpar()

    minimo = 1
    maximo = 100
    tentativas = 0

    print("==============================")
    print("  JOGO BINÁRIO DE ADIVINHAÇÃO ")
    print("==============================")
    print("\nPense em um número entre 1 e 100.")
    print("Responda com:")
    print("- 'muito alto'  (>10 acima)")
    print("- 'alto'        (1 a 10 acima)")
    print("- 'baixo'       (1 a 10 abaixo)")
    print("- 'muito baixo' (>10 abaixo)")
    print("- 'sim'         (acertou)\n")



    while True:
        chute = calcular_chute(minimo, maximo)
        tentativas += 1

        resposta = input(f"O número é {chute}? ").strip().lower()

        if not validar_resposta(resposta):
            print("Resposta inválida. Tente novamente.\n")
            continue

        if resposta == 'sim':
            print(f"\nAcertei em {tentativas} tentativas!")
            break

        elif resposta == 'muito alto':
            maximo = chute - 11

        elif resposta == 'alto':
            maximo = chute - 1

        elif resposta == 'baixo':
            minimo = chute + 1

        elif resposta == 'muito baixo':
            minimo = chute + 11

        if minimo > maximo:
            print("\nAlgo deu errado nas respostas.")
            print("Verifique se você respondeu corretamente.")
            break
