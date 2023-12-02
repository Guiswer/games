#Jogo da velha - desafio 7.10 do livro Introdução à programação com Python, do autor Nilo Ney Coutinho Menezes
#Desenvolvido por: Guiswer
#Interface pelo terminal

import os

# Procedimento para limpar o terminal
def limpar_terminal():
	if os.name == 'posix':
		os.system("clear")

	elif os.name == 'nt':
		os.system("cls")


def matriz():
	print(f"""
	      {tabuleiro[0][0]}| {tabuleiro[0][1]} |{tabuleiro[0][2]}
	     --+---+--
	      {tabuleiro[1][0]}| {tabuleiro[1][1]} |{tabuleiro[1][2]} 
	     --+---+--
	      {tabuleiro[2][0]}| {tabuleiro[2][1]} |{tabuleiro[2][2]} 
	""")


def entrada_jogador1():
	escolha_player1 = int(input("Jogador 1, digite a posição que deseja jogar: "))
	return escolha_player1


def entrada_jogador2():
	escolha_player2 = int(input("Jogador 2, digite a posição que deseja jogar: "))
	return escolha_player2


vencedor1 = "Player 1"
vencedor2 = "Player 2"
def ganhou(vencedor):
	print(f"Parabéns {vencedor}, você ganhou!")


def verificador1(choice_player1):

	if choice_player1 == 1 and tabuleiro[2][0] == "-":
		tabuleiro[2][0] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 2 and tabuleiro[2][1] == "-":
		tabuleiro[2][1] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 3 and tabuleiro[2][2] == "-":
		tabuleiro[2][2] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 4 and tabuleiro[1][0] == "-":
		tabuleiro[1][0] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 5 and tabuleiro[1][1] == "-":
		tabuleiro[1][1] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 6 and tabuleiro[1][2] == "-":
		tabuleiro[1][2] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 7 and tabuleiro[0][0] == "-":
		tabuleiro[0][0] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 8 and tabuleiro[0][1] == "-":
		tabuleiro[0][1] = "X"
		limpar_terminal()
		matriz()

	elif choice_player1 == 9 and tabuleiro[0][2] == "-":
		tabuleiro[0][2] = "X"
		limpar_terminal()
		matriz()




def verificador2(choice_player2):

	if choice_player2 == 1 and tabuleiro[2][0] == "-":
		tabuleiro[2][0] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 2 and tabuleiro[2][1] == "-":
		tabuleiro[2][1] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 3 and tabuleiro[2][2] == "-":
		tabuleiro[2][2] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 4 and tabuleiro[1][0] == "-":
		tabuleiro[1][0] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 5 and tabuleiro[1][1] == "-":
		tabuleiro[1][1] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 6 and tabuleiro[1][2] == "-":
		tabuleiro[1][2] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 7 and tabuleiro[0][0] == "-":
		tabuleiro[0][0] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 8 and tabuleiro[0][1] == "-":
		tabuleiro[0][1] = "O"
		limpar_terminal()
		matriz()


	elif choice_player2 == 9 and tabuleiro[0][2] == "-":
		tabuleiro[0][2] = "O"
		limpar_terminal()
		matriz()


def verificador_marcação_player1(choice_player1):

	if choice_player1 == 1 and tabuleiro[2][0] != "-" or choice_player1 == 2 and tabuleiro[2][1] != "-" or choice_player1 == 3 and tabuleiro[2][2] != "-" or choice_player1 == 4 and tabuleiro[1][0] != "-" or choice_player1 == 5 and tabuleiro[1][1] != "-" or choice_player1 == 6 and tabuleiro[1][2] != "-" or choice_player1 == 7 and tabuleiro[0][0] != "-" or choice_player1 == 8 and tabuleiro[0][1] != "-" or choice_player1 == 9 and tabuleiro[0][2] != "-":

		limpar_terminal()
		matriz()
		print("Este lugar já foi marcado!")
		print(choice_player1)
		choice_player1 = entrada_jogador1()

def verificador_marcação_player2(choice_player2):

	if choice_player2 == 1 and tabuleiro[2][0] != "-" or choice_player2 == 2 and tabuleiro[2][1] != "-" or choice_player2 == 3 and tabuleiro[2][2] != "-" or choice_player2 == 4 and tabuleiro[1][0] != "-" or choice_player2 == 5 and tabuleiro[1][1] != "-" or choice_player2 == 6 and tabuleiro[1][2] != "-" or choice_player2 == 7 and tabuleiro[0][0] != "-" or choice_player2 == 8 and tabuleiro[0][1] != "-" or choice_player2 == 9 and tabuleiro[0][2] != "-":
		limpar_terminal()
		matriz()
		print("Este lugar já foi marcado!")
		print(choice_player1)
		choice_player1 = entrada_jogador1()


def verificador_vitória_player1(tabuleiro):

	# Condições de fim de jogo
	# Jogador 1 vencedor

	var = False

	# HORIZONTAL/VERTICAL/DIAGONAL
	if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X" or tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X" or tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X" or tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X" or tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X" or tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X" or  tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X" or tabuleiro[0][2] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][0] == "X":
		ganhou(vencedor1)

		var = True
		return var

def verificador_vitória_player2(tabuleiro):

	# Condições de fim de jogo
	# Jogador 2 vencedor

	var = False

	# HORIZONTAL/VERTICAL/DIAGONAL
	if tabuleiro[0][0] == "O" and tabuleiro[0][1] == "O" and tabuleiro[0][2] == "O" or tabuleiro[1][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[1][2] == "O" or tabuleiro[2][0] == "O" and tabuleiro[2][1] == "O" and tabuleiro[2][2] == "O" or tabuleiro[0][0] == "O" and tabuleiro[1][0] == "O" and tabuleiro[2][0] == "O" or tabuleiro[0][1] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][1] == "O" or tabuleiro[0][2] == "O" and tabuleiro[1][2] == "O" and tabuleiro[2][2] == "O" or  tabuleiro[0][0] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][2] == "O" or tabuleiro[0][2] == "O" and tabuleiro[1][1] == "O" and tabuleiro[2][0] == "O":
		ganhou(vencedor2)

		var = True
		return var

def verificador_empate(contador_jogadas):

	if contador_jogadas == 9:
		print("O jogo empatou! 🏳️")
		

print("Bem-vindo ao jogo da velha! 😄 \n")
print("Jogador 1 = ✖ (X)\nJogador 2 = ⚬ (O)\n")
print('Posições do "tabuleiro" ')
print(""" 
       7| 8 |9
       -+---+-
       4| 5 |6 
       -+---+-
       1| 2 |3 
""")


tabuleiro = [["-"]*3 for i in range(3)]

var1 = verificador_vitória_player1(tabuleiro)
var2 = verificador_vitória_player2(tabuleiro)

contador_jogadas = 0


# Inicio do jogo

while True: 

	# Condicionais para o jogador 1 

	choice_player1 = entrada_jogador1()
	verificador_marcação_player1(choice_player1)
	verificador1(choice_player1)

	verificador_vitória_player1(tabuleiro)
	if var1:
		break

	contador_jogadas += 1 
	verificador_empate(contador_jogadas)


	# Condicionais para o jogador 2 

	choice_player2 = entrada_jogador2()
	verificador_marcação_player2(choice_player2)
	verificador2(choice_player2)

	verificador_vitória_player2(tabuleiro)
	if var2:
		break	

	contador_jogadas += 1
	verificador_empate(contador_jogadas)


print("Jogo encerrado.\nObrigado por jogar! 😅")