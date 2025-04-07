
board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(' | '.join(row))
        if i < 2:
            print('--+---+--')
    print()

def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
def check_draw():
    return all(cell != ' ' for cell in board)


def play_game():
    current_player = 'X'

    while True:
        print_board()

        try:
            move = int(
                input(f'player {current_player}, select between (1-9): ')
            ) - 1
        except ValueError:
            print('i said numbers...')
            continue

        if move < 0 or move > 8:
            print('it should be between 1-9')
            continue
        if board[move] != ' ':
            print('this window is taken')
            continue
        board[move] = current_player

        is_winner = check_winner(current_player)
        if is_winner:
            print_board()
            print(f'player: {current_player} won!')
            break

        is_draw = check_draw()
        if is_draw:
            print_board()
            print('Its a draw')
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()