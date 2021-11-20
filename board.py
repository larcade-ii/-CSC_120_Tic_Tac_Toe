
import random


class TicTacToe:

    def __init__(initial):
        initial.board = []

    def create_board(initial):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            initial.board.append(row)

    def get_random_first_player(initial):
        return random.randint(0, 1)

    def fix_spot(initial, row, col, player):
        initial.board[row][col] = player

    def winning_player(initial, player):
        win = None

        n = len(initial.board)

        # horizontal win condition
        for i in range(n):
            win = True
            for j in range(n):
                if initial.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # vertical win condition
        for i in range(n):
            win = True
            for j in range(n):
                if initial.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # diagonal win condition
        win = True
        for i in range(n):
            if initial.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if initial.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in initial.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(initial):
        for row in initial.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(initial, player):
        return 'X' if player == 'O' else 'O'

    def show_board(initial):
        for row in initial.board:
            for item in row:
                print(item, end=" ")
            print()

    def begin(initial):
        initial.create_board()

        player = 'X' if initial.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            initial.show_board()

            # taking user input
            row, col = list(
                map(int, input("Please enter a row and column number (Separated by a Space): ").split()))
            print()

            # fixing the spot
            initial.fix_spot(row - 1, col - 1, player)

            # Current Win Condition?
            if initial.winning_player(player):
                print(f"Player {player} wins!")
                break

            # checking whether the game is draw or not
            if initial.is_board_filled():
                print("Match Draw!")
                break


            player = initial.swap_player_turn(player)


        print()
        initial.show_board()


# begin
tic_tac_toe = TicTacToe()
tic_tac_toe.begin()
