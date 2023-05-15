class Cell:

    def __init__(self, number, busy=False):
        self.number = number
        self.busy = busy


class Board:

    def __init__(self):
        self.board = [Cell(i) for i in range(1, 10)]

    def print_board(self):
        print('-' * 13)

        for i in range(3):
            print('|', self.board[0 + i * 3].number, '|',
                  self.board[1 + i * 3].number, '|',
                  self.board[2 + i * 3].number, '|')

        print('-' * 13)

    def check_busy(self, number):

        if self.board[number - 1].busy:
            return True
        else:
            return False

    def check_win(self):
        win_coordinate = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                          (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

        for coordinate in win_coordinate:
            if (self.board[coordinate[0]].number ==
                    self.board[coordinate[1]].number):
                if (first_player.symb == self.board[coordinate[0]].number):
                    print(f"Победил {first_player.name}")
                elif (second_player.symb == self.board[coordinate[0]].number):
                    print(f"Победил {second_player.name}")


class Player:

    def __init__(self, name, symb, win=False):
        self.name = name
        self.symb = symb
        self.win = win

    def cell_selection(self, number, Board):
        Board.board[number - 1].busy = True
        Board.board[number - 1].number = self.symb


first_player = Player("Андрей", 'X')
second_player = Player("Егор", 'O')
board = Board()
count = 0


def Game(player, board):
    number = int(input(f"Выбирайте клетку куда хотите сходить, {player.name}: "))

    if board.check_busy(number):
        print("Клетка занята")
        Game(player, board)
    else:
        player.cell_selection(number, board)


while True:
    board.print_board()

    if count % 2 == 0:
        Game(first_player, board)
        if board.check_win():
            break
        else:
            Game(second_player, board)
            if board.check_win():
                break

    count += 1

    if count == 9:
        print("Ничья")
        break