from modo_jogador import jogar as jogo_usuario
from modo_computador import jogar as jogo_binario

while True:
    print("\n=== JOGO DE ADIVINHAÇÃO ===")
    print("[1] Jogar (usuário adivinha)")
    print("[2] Jogar (computador adivinha)")
    print("[0] Sair")

    opcao = input("Escolha: ")

    if opcao == '1':
        jogo_usuario()
    elif opcao == '2':
        jogo_binario()
    elif opcao == '0':
        break
    else:
        print("Opção inválida.")