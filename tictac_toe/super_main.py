
class SmallBoard:
    def __init__(self):
        self.cels = [' ' for _ in range(9)]
        self.winner = None



    def make_move(self, index, player):
        if self.cels[index] == ' ':
            self.cels[index] = player
            self.check_winner(player)
            return True
        return False

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_combinations:
            if all(self.cels[i] == player for i in combo):
                self.winner = player
                return
        if_full = self.is_full()
        if if_full:
            self.winner = 'D'

        if all(cell != ' ' for cell in self.cels):
            self.winner = 'D'

    def is_full(self):
        return all(cell != ' ' for cell in self.cels)

    def is_active(self):
        return self.winner is None

class UltimateTicTacToe:
    def __init__(self):
        self.boards = [SmallBoard() for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
        self.active_board = None

    def display(self):
        print()
        for big_row in range(3):
            for small_row in range(3):
                row = []
                for big_column in range(3):
                    board_index = big_row * 3 + big_column
                    board = self.boards[board_index]
                    row_cels = board.cels[small_row * 3:(small_row+1) *3]
                    row.append(' | '.join(row_cels))
                print(' || '.join(row))
            if big_row < 2:
                print('=' * 35)
        print()

    def check_ovearll_winner(self):
        winners = [b.winner if b.winner in ['X', 'O'] else ' ' for b in self.boards]
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            line = [winners[i] for i in combo]
            if line[0] != ' ' and all(w == line[0] for w in line):
                self.winner = line[0]
                return

    def make_move(self, board_index, cell_index):
        if board_index < 0 or board_index >= 9 or cell_index < 0 or cell_index >=9:
            print('wrong table or table number')
            return False

        board = self.boards[board_index]
        is_active = board.is_active()
        if not is_active:
            print('this table is done')
            return False

        if not board.make_move(cell_index, self.current_player):
            print('this window is already taken')

        self.check_ovearll_winner()
        self.active_board = cell_index if self.boards[cell_index].is_active() else None
        self.current_player = 'O' if self.current_player == 'X' else 'X'



    def is_draw(self):
        return all(board.winner is not None for board in self.boards) and self.winner is None

    def play(self):
        while self.winner is None and not self.is_draw():
            self.display()
            print(f'Player {self.current_player} turn')
            if self.active_board is not None:
                print(f'You must play in {self.active_board + 1}')
            else:
                print('You can choose any active window')

            try:
                if self.active_board is not None:
                    board_index = self.active_board
                else:
                    board_index = int(input('Enter small window nr from 1 to 9:')) - 1
                cell_index = int(input('Enter window number from 1 to 9:')) - 1
            except ValueError:
                print('Enter a number dummy')
                continue


            move= self.make_move(board_index, cell_index)
            if not move:
                continue
            self.display()
            if self.winner:
                print(f'player {self.winner} won')
            else:
                print('its a draw?')



game = UltimateTicTacToe()
game.play()


# def print_board():
#     print()
#     for i in range(3):
#         row = board[i*3:(i+1)*3]
#         print(' | '.join(row))
#         if i < 2:
#             print('--+---+--')
#     print()
#
# def check_winner(player):
#     win_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],
#         [0, 4, 8], [2, 4, 6]
#     ]
#     for combo in win_combinations:
#         if all(board[i] == player for i in combo):
#             return True
#     return False
# def check_draw():
#     return all(cell != ' ' for cell in board)
#
#
# def play_game():
#     current_player = 'X'
#
#     while True:
#         print_board()
#
#         try:
#             move = int(
#                 input(f'player {current_player}, select between (1-9): ')
#             ) - 1
#         except ValueError:
#             print('i said numbers...')
#             continue
#
#         if move < 0 or move > 8:
#             print('it should be between 1-9')
#             continue
#         if board[move] != ' ':
#             print('this window is taken')
#             continue
#         board[move] = current_player
#
#         is_winner = check_winner(current_player)
#         if is_winner:
#             print_board()
#             print(f'player: {current_player} won!')
#             break
#
#         is_draw = check_draw()
#         if is_draw:
#             print_board()
#             print('Its a draw')
#             break
#
#         current_player = 'O' if current_player == 'X' else 'X'
#
# play_game()