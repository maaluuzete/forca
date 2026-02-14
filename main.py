import random
import sys

def load_words(filename):
    """Lê as palavras do arquivo e retorna uma lista."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            words = [line.strip().upper() for line in file if line.strip()]
        
        if not words:
            print(f"Erro: O arquivo '{filename}' está vazio.")
            sys.exit(1)
            
        return words
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
        sys.exit(1)

def display_game_state(secret_word, guessed_letters, attempts_left):
    """Exibe o progresso da palavra, tentativas e letras já usadas."""
    display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("\n" + "="*30)
    print(f"Palavra: {' '.join(display_word)}")
    print(f"Tentativas restantes: {attempts_left}")  
    if guessed_letters:
        print(f"Letras tentadas: {', '.join(sorted(guessed_letters))}")
    else:
        print("Letras tentadas: Nenhuma")
    print("="*30)

def get_valid_input(guessed_letters):
    """Solicita e valida a entrada do jogador."""
    while True:
        guess = input("\nDigite uma letra: ").strip().upper() 
        if len(guess) != 1 or not guess.isalpha():
            print("Entrada inválida! Por favor, digite apenas uma letra.")
        elif guess in guessed_letters:
            print(f"Você já tentou a letra '{guess}'. Escolha outra.")
        else:
            return guess

def main():
    print("Bem-vindo ao Jogo da Forca!")
    words= load_words("palavras.txt")
    secret_word =random.choice(words)
    guessed_letters = set()
    attempts_left=6
    while attempts_left > 0:
        display_game_state(secret_word, guessed_letters, attempts_left)      
        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess) 
        if guess in secret_word:
            print(f"Boa! A letra '{guess}' está na palavra.")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\nParabéns! Você acertou a palavra: {secret_word}")
                return
        else:
            attempts_left -= 1
            print(f"A letra '{guess}' não está na palavra.")
    print(f"\nFim de jogo! A palavra era: {secret_word}")

if __name__ == "__main__":
    main()