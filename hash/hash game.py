#Jogo da velha - exercício 7.10 do livro Introdução à programação com Python, do autor Nilo Ney Coutinho Menezes
#Desenvolvido por: Guiswer
#Interface pelo terminal

import os

# procedimento para limpar o terminal
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
	choice_player1 = int(input("Jogador 1, digite a posição que deseja jogar: "))
	return choice_player1

def entrada_jogador2():
	choice_player2 = int(input("Jogador 2, digite a posição que deseja jogar: "))
	return choice_player2


def ganhou(vencedor):
	print("Parabéns {}, você ganhou!")


print("Bem-vindo ao jogo da velha!\n")
print("Jogador 1 = X\nJogador 2 = O\n")
print('Posições do "tabuleiro" ')
print(""" 
       7| 8 |9
       -+---+-
       4| 5 |6 
       -+---+-
       1| 2 |3 
""")

tabuleiro = [["-"]*3 for i in range(3)]

while True: 

	# condicionais para o jogador 1 

	choice_player1 = entrada_jogador1()

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

	else:
		limpar_terminal()
		matriz()
		print("Este lugar já foi marcado!")
		print(choice_player1)
		continue


	# condicionais para o jogador 2 

	choice_player2 = entrada_jogador2()

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

	else:
		limpar_terminal()
		matriz()
		print("Este lugar já foi marcado!")
		print(choice_player1)
		continue