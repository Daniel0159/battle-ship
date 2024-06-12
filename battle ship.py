import random

# Translation dictionaries
translations = {
    "en": {
        "welcome": "Let's play Battleship!",
        "choose_mode": "Choose a game mode (1-3): ",
        "user_vs_user": "User vs User",
        "user_vs_pc": "User vs PC",
        "pc_vs_pc": "PC vs PC",
        "guess_row": "Guess Row (0-4):",
        "guess_col": "Guess Col (0-4):",
        "congratulations": "Congratulations! You sank my battleship!",
        "not_in_ocean": "Oops, that's not even in the ocean.",
        "guessed": "You guessed that one already.",
        "missed": "You missed my battleship!",
        "game_over": "Game Over",
        "play_again": "Do you want to play again? (yes/no): "
    },
    "pt": {
        "welcome": "Vamos jogar Battleship!",
        "choose_mode": "Escolha um modo de jogo (1-3): ",
        "user_vs_user": "Usuário vs Usuário",
        "user_vs_pc": "Usuário vs PC",
        "pc_vs_pc": "PC vs PC",
        "guess_row": "Adivinhe a linha (0-4):",
        "guess_col": "Adivinhe a coluna (0-4):",
        "congratulations": "Parabéns! Você afundou meu navio de guerra!",
        "not_in_ocean": "Opa, isso nem está no oceano.",
        "guessed": "Você já adivinhou isso.",
        "missed": "Você perdeu meu navio de guerra!",
        "game_over": "Fim de jogo",
        "play_again": "Você quer jogar de novo? (sim/não): "
    }
}

while True:
    # Choose language
    lang = input("Choose a language (en/pt): ")
    if lang not in translations:
        lang = "en"
    t = translations[lang]

    # Choose game mode
    print(t["choose_mode"])
    print("1. " + t["user_vs_user"])
    print("2. " + t["user_vs_pc"])
    print("3. " + t["pc_vs_pc"])
    mode = input()

    # Initialize the board
    board = []
    for x in range(0, 5):
      board.append(["O"] * 5)

    def print_board(board):
      for row in board:
        print(" ".join(row))

    print(t["welcome"])
    print_board(board)

    def random_row(board):
      return random.randint(0,len(board)-1)

    def random_col(board):
      return random.randint(0,len(board[0])-1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    # Game loop
    for turn in range(4):
      print("Turn", turn + 1)
      if mode == '1' or mode == '2':
        guess_row = int(input(t["guess_row"]))
        guess_col = int(input(t["guess_col"]))
      else:
        guess_row = random_row(board)
        guess_col = random_col(board)

      if guess_row == ship_row and guess_col == ship_col:
        print(t["congratulations"])
        break
      else:
        if guess_row not in range(5) or \
          guess_col not in range(5):
          print(t["not_in_ocean"])
        elif board[guess_row][guess_col] == "X":
          print(t["guessed"])
        else:
          print(t["missed"])
          board[guess_row][guess_col] = "X"
        if (turn == 3):
          print(t["game_over"])
        print_board(board)

    play_again = input(t["play_again"])
    if play_again.lower() not in ["yes", "sim"]:
        break