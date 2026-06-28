import random as rdm
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Inicialização das variáveis globais
Pontos = 1000
Tentativas = 1
UsarPontos = True  # Nova variável global para rastrear a escolha do usuário

print(r"""
==================================================
         POTUATION - TERMINAL EDITION
==================================================
""")

def Pontuação():
    global UsarPontos
    while True:
        resposta = input(r"""
+--------------------------------------+
|           SISTEMA DE PONTOS          |
+--------------------------------------+
| Deseja jogar com pontuacao?          |
|                                      |
| [1] Sim                              |
| [2] Não                              |
+--------------------------------------+

> """)
        limpar()
        if resposta == "1":
            print("\n[+] Pontuacao ativada.\n")
            UsarPontos = True
            break
        elif resposta == "2":
            print("\n[-] Pontuacao desativada.\n")
            UsarPontos = False
            break
        else:
            print("\n[!] Use apenas 1 ou 2.\n")

def Seleção():
    while True:  # Adicionado loop para garantir que o usuário escolha uma opção válida
        resposta = input(r"""
+--------------------------------------+
|            MENU PRINCIPAL            |
+--------------------------------------+
| [1] Modo Acerto                      |
| [2] Modo Soma                        |
| [3] Modo Multiplicacao               |
+--------------------------------------+

Escolha um modo:
> """)
        limpar()
        if resposta == "1":
            print("\n[+] Modo de acerto selecionado.\n")
            return resposta
        elif resposta == "2":
            print("\n[+] Modo de soma selecionado.\n")
            return resposta
        elif resposta == "3":
            print("\n[+] Modo de multiplicacao selecionado.\n")
            return resposta
        else:
            print("\n[!] Opcao invalida. Tente novamente.\n")

def MainGuess():
    global Tentativas, Pontos, UsarPontos

    number = rdm.randint(1, 100)

    print(r"""
+--------------------------------------+
|             MODO ACERTO              |
+--------------------------------------+
| Escolhi um numero entre 1 e 100.     |
| Tente adivinhar!                     |
+--------------------------------------+
""")
    while True:
        try:
            guess = int(input(">>> Seu chute: "))

            if guess < 1 or guess > 100:
                print("\n[!] Numero fora do intervalo.\n")
                continue

            if guess < number:
                print(r"""
    ↓
    ↓
    ↓

Muito baixo!
""")
                Tentativas += 1

            elif guess > number:
                print(r"""
    ↑
    ↑
    ↑

Muito alto!
""")
                Tentativas += 1

            else:
                print(rf"""
========================================
             VOCE VENCEU!
========================================

Numero encontrado: {number}
Tentativas: {Tentativas}
""")
                if UsarPontos:
                    pontuacao_final = max(0, Pontos - (Tentativas * 10))
                    print(f"Sua pontuação final foi: {pontuacao_final}")
                
                print("========================================\n")
                break

        except ValueError:
            print("\n[!] Digite um numero inteiro.\n")

def MainSoma():
    global Tentativas, Pontos, UsarPontos

    number = rdm.randint(1, 100)
    gapMin = -10
    gapMax = 10

    print(r"""
+--------------------------------------+
|              MODO SOMA               |
+--------------------------------------+
| Escolhi um numero secreto.           |
| Use somas para obter pistas.         |
+--------------------------------------+
""")
    
    while True:
        try:
            guess = int(input(">>> Numero para somar (Entre 35 e 125): "))
            if guess < 35 or guess > 125:
                print("\n[!] Numero fora do intervalo.\n")
                continue

            print("\n+----------- PISTA -----------+")
            print(
                f"Meu numero + {guess} esta entre "
                f"{guess + number + gapMin} e "
                f"{guess + number + gapMax}"
            )
            print("+-----------------------------+\n")

            resposta = int(input(">>> Qual e o meu numero? "))

            if resposta < number:
                print("\n[↓] Muito baixo!\n")
                Tentativas += 1

            elif resposta > number:
                print("\n[↑] Muito alto!\n")
                Tentativas += 1

            else:
                print(rf"""
========================================
             VOCE VENCEU!
========================================

Numero encontrado: {number}
Tentativas: {Tentativas}
""")
                if UsarPontos:
                    pontuacao_final = max(0, Pontos - (Tentativas * 10))
                    print(f"Sua pontuação final foi: {pontuacao_final}")
                
                print("========================================\n")
                break

        except ValueError:
            print("\n[!] Digite um numero inteiro.\n")

def MainMult():
    global Tentativas, Pontos, UsarPontos
    number = rdm.randint(1, 100)
    
    print(r"""
+--------------------------------------+
|          MODO MULTIPLICACAO          |
+--------------------------------------+
| Escolhi um numero entre 1 e 100.     |
| Use mutiplicações como pistas.       |
+--------------------------------------+
""")
    
    # O input do multiplicador foi movido para dentro do try/except para evitar erros caso digitem letras
    while True:
        try:
            mult = int(input(">>> Numero para multiplicar (Entre 9 e 17): "))
            if mult < 9 or mult > 17:
                print("\n[!] Numero fora do intervalo.\n")
                continue
            break
        except ValueError:
            print("\n[!] Digite um numero inteiro.\n")

    while True:
        try:
            print ("\n+----------- PISTA -----------+")
            print(      f"Meu numero * {mult} esta entre "
                f"{mult * number - 10} e "
                f"{mult * number + 10}"
            )
            print("+-----------------------------+\n")
            
            guess = int(input(">>> Seu chute: "))
            if guess < number:
                print(r"""
    ↓
    ↓
    ↓

Muito baixo!
""")
                Tentativas += 1

            elif guess > number:
                print(r"""
    ↑
    ↑
    ↑

Muito alto!
""")
                Tentativas += 1

            else:
                print(rf"""
========================================
             VOCE VENCEU!
========================================

Numero encontrado: {number}
Tentativas: {Tentativas}
""")
                if UsarPontos:
                    pontuacao_final = max(0, Pontos - (Tentativas * 10))
                    print(f"Sua pontuação final foi: {pontuacao_final}")
                
                print("========================================\n")
                break

        except ValueError:
            print("\n[!] Digite um numero inteiro.\n")

def Atuação():
    modo = Seleção()

    if modo == "1":
        MainGuess()
    elif modo == "2":
        MainSoma()
    elif modo == "3":
        MainMult()

# Execução do jogo
Pontuação()
Atuação()