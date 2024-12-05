# Projeto 1 - Jogo da forca 

# Import
import random 
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

	# Windows
	if name == 'nt':
		_= system('cls')

	# Mac ou Linux
	else:
		_= system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Função do jogo
def game():

    limpa_tela()
    print("\nBem vindo(a) ao jogo da forca!")

    # Categorias (minha adição ao código)
    animais = ['peixe', 'macaco', 'elefante', 'gato', 'cachorro']
    comidas = ['chocolate', 'morango', 'pizza', 'sorvete', 'espaguete']
    paises = ['brasil', 'argentina', 'japao', 'alemanha', 'russia']
    atividades = ['leitura', 'programacao', 'cozinhar', 'passear', 'dormir']

    # Laço para testar categoria válida
    while True:
        print("""\nOpções:
        1 - Animais
        2 - Comidas
        3 - Países
        4 - Atividades""")

        categoria = int(input("\nSelecione a categoria(número):"))

        # Escolha aleatória de palavras dentro de uma categoria
        if categoria == 1:
            print("Você escolheu animais! Tente acertar a palavra.")
            palavra = random.choice(animais)
        elif categoria == 2:
            print("Você escolheu comidas! Tente acertar a palavra.")
            palavra = random.choice(comidas)
        elif categoria == 3:
            print("Você escolheu países! Tente acertar a palavra.")
            palavra = random.choice(paises)
        elif categoria == 4:
            print("Você escolheu atividades! Tente acertar a palavra.")
            palavra = random.choice(atividades)
        else:
            print("Categoria inválida!")

        if categoria >= 1 and categoria <= 4:
            break
	
	# List comprehension
    letras_descobertas = ['_' for letra in palavra]

	# Número de chances
    chances = 6

	# Lista para letras erradas
    letras_erradas = []

	# Loop enquanto número de chances for maior que zero
    while chances > 0:

        print(display_hangman(chances))
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

		# Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            print("Ops. Essa letra não está na palavra!")
            chances -= 1
            letras_erradas.append(tentativa)

		# Conclusão

        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu! A palavra era:", palavra)

if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo python com a DSA :)\n")