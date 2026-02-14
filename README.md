## Hangman Game
A classic command-line Hangman game developed using pure Python. This project challenges players to guess a hidden word letter by letter within a limited number of attempts. The game selects a random word from a local text file and displays it as a series of underscores. For every correct guess, the word is updated to reveal the letters. For every incorrect guess, the number of remaining attempts decreases. The game includes input validation to ensure only single alphabetic characters are processed and keeps track of all previously guessed letters to prevent duplicates.

## Project Structure

```forca/
├── LICENSE
├── README.md
├── main.py
└── words.txt
```