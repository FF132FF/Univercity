class Board:

    def __init__(self):
        self.board = {
                "TL": " ", "TM": " ", "TR": " ",
                "ML": " ", "MM": " ", "MR": " ",
                "BL": " ", "BM": " ", "BR": " "}

    def printBoard(self):
        print(self.board["TL"] + "|" + self.board["TM"] + "|" + self.board["TR"])
        print("-+-+-")
        print(self.board["ML"] + "|" + self.board["MM"] + "|" + self.board["MR"])
        print("-+-+-")
        print(self.board["BL"] + "|" + self.board["BM"] + "|" + self.board["BR"])

    def isValidMove(self, position):
        if self.board[position] == " ":
            return True
        return False

    def changeBoard(self, position, type):
        if self.isValidMove(position):
            self.board[position] = type
            return self.board
        return None

    def isWinner(self, player):
        if self.board["TL"] == player.type and self.board["TM"] == player.type and self.board["TR"] == player.type or \
        self.board["ML"] == player.type and self.board["MM"] == player.type and self.board["MR"] == player.type or \
        self.board["BL"] == player.type and self.board["BM"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["ML"] == player.type and self.board["BL"] == player.type or \
        self.board["TM"] == player.type and self.board["MM"] == player.type and self.board["BM"] == player.type or \
        self.board["TR"] == player.type and self.board["MR"] == player.type and self.board["BR"] == player.type or \
        self.board["TL"] == player.type and self.board["MM"] == player.type and self.board["BR"] == player.type or \
        self.board["BL"] == player.type and self.board["MM"] == player.type and self.board["TR"] == player.type:
            return True
        return False


class Player:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return "Player {}".format(self.type)


class Game:
    def __init__(self):
        self.firstPlayer = Player("X")
        self.secondPlayer = Player("O")
        self.board = Board()

    def printValidEntries(self):
        print("""
            TL | TM | TR 
            ML | MM | MR 
            BL | BM | BR """)

    def printingBoard(self):
        self.board.printBoard()

    def changeTurn(self, player):
        if player == self.firstPlayer:
            return self.secondPlayer
        else:
            return self.firstPlayer

    def wonGame(self, player):
        return self.board.isWinner(player)

    def modifyBoard(self, position, type):
        if self.board.changeBoard(position, type) is not None:
            return self.board.changeBoard(position, type)
        else:
            position = input("Not available position. Please, try again: ")
            return self.board.changeBoard(position, type)

    def existenceCheck(self, position):
        existingCells = ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]
        if position in existingCells:
            return position
        else:
            while position not in existingCells:
                print(f"Cell with this name: {position} dose not exist. Please, write the name of an exiting cell: ")
                print("""
                            TL | TM | TR 
                            ML | MM | MR 
                            BL | BM | BR """)
                position = input("What's your move? ")
            return position

def play():
    game = Game()
    game.printValidEntries()
    player = game.firstPlayer
    number = 9
    while number > 0:
        number -= 1
        game.printingBoard()
        position = input("{} turn, what's your move? ".format(player))
        game.modifyBoard(game.existenceCheck(position), player.type)
        if game.wonGame(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = game.changeTurn(player)
    if number == 0:
        print("Game over! It's a tie!")

play()