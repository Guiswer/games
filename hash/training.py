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
	      --+----+--
	      {tabuleiro[1][0]}| {tabuleiro[1][1]} |{tabuleiro[1][2]} 
	      --+----+--
	      {tabuleiro[2][0]}| {tabuleiro[2][1]} |{tabuleiro[2][2]} 
	""")

def entrada_jogador1():
	choice_player1 = int(input("Jogador 1, digite a posição que deseja jogar: "))
	return choice_player1

def entrada_jogador2():
	choice_player2 = int(input("Jogador 2, digite a posição que deseja jogar: "))
	return choice_player2

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

	entrada_jogador1()

	if choice_player == 1 and tabuleiro[2][0] == "-":
		tabuleiro[2][0] = "X"
		matriz()
	else:
		print("Este lugar já foi marcado!")
		continue


	tabuleiro[choice_player1] = "X"

	limpar_terminal()
	matriz()

print(tabuleiro)
