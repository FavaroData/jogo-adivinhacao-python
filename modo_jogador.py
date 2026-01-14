import random
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def jogar():

    lista_numeros = list(range(1, 101))

    numero_escolhido = random.randint(1, 101)
    tentativas = 0

    limpar()

    print("\n========================")
    print("  JOGO DE ADIVINHAÇÃO")
    print("========================")
    print("\nEu escolhi um número entre 1 e 100, e você tem que adivinhar!")

    while True:
        print(f"Tentativas: {tentativas}")
        print("\nTente adivinhar o número que estou pensando:")
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa == numero_escolhido:
            print("\nVocê Acertou!")
            print(f'Suas tentativas: {tentativas}\n')
            break

        elif numero_escolhido < tentativa == numero_escolhido + 1:
            print(f"\n{tentativa} é Bemmmmm perto")

        elif numero_escolhido > tentativa == numero_escolhido - 1:
            print(f"\n{tentativa} é muito muito perto")

        elif numero_escolhido < tentativa <= numero_escolhido + 10:
            print(f"\n{tentativa} é Alto")

        elif tentativa > numero_escolhido + 10:
            print(f"\n{tentativa} é Muito Alto")

        elif numero_escolhido - 10 <= tentativa < numero_escolhido:
            print(f"\n{tentativa} é Baixo")

        else:
            print(f"\n{tentativa} é Muito Baixo")

