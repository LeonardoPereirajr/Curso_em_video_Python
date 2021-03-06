# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = [''' >>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor

	def __init__(self, palavra):
		self.palavra = palavra
		self.errada_letra = []
		self.certa_letra = []
		
	# Método para adivinhar a letra
	def guess(self, letra):
		if letra in self.palavra and letra not in self.certa_letra:
			self.certa_letra.append(letra)
		elif letra not in self.palavra and letra not in self.errada_letra:
			self.errada_letra.append(letra)
		else:
			return False
		return True
		
	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.errada_letra) == 6) # existe 6 tentivas
		
	# Método para verificar se o jogador venceu se ainda tiver '_'  na hide_word
	def hangman_won(self):
		if '_' not in self.hide_word():
			return True
		return False
		
	# Método para mostrar ou não a letra no board
	def hide_word(self):
		rtn = ''
		for letra in self.palavra:
			if letra not in self.certa_letra:
				rtn += '_' # mostra '_"
			else:
				rtn += letra #mostra a letra
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.errada_letra)])# tras os elementos da lista errada de acordo com o tamanho desta lista
		print('\nPalavra: ' + self.hide_word())
		print('\nLetras erradas: ',)
		for letra in self.errada_letra:
			print (letra,)
		print()
		print('Letras corretas: ',)
		for letra in self.certa_letra:
			print(letra,)
		print()

# Método para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()

# Método Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		user_input = input('\nDigite uma letra: ')
		game.guess(user_input)

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.palavra)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()
