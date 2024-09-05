class Game:

    def __create_game(self):
        self.player1 = 'x'
        self.player2 = '0'
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ', ' ']

    def start_game(self):
        self.__create_game()
        for move in range(len(self.board)):
            check_victory = lambda player1, player2: ((self.__motion_players(player1) and self.__user_victory(player1)) or\
            (self.__motion_players(player2) and self.__user_victory(player2)))
            if check_victory(self.player1, self.player2) is True:
                break

    def __motion_players(self, player):
        while True:
            try:
                print(f'Ходит {player}')
                motion = int(input('Введите номер клетки: '))
                if self.board[motion] == ' ' and motion > self.board.index(' ', 0):
                    self.board[motion] = player
                    print(self.board[1:4], self.board[4:7], self.board[7:10], sep='\n')
                    return True
                else:
                    print('Эта ячейка уже занята, или её не существует.')
            except (ValueError, IndexError):
                    print('Ошибка.')

    def __user_victory(self, player):
        lst = [player, player, player]
        if ((self.board[1:4] == lst or self.board[4:7] == lst or self.board[7:10] == lst) or
                (self.board[1:8:3] == lst or self.board[2:9:3] == lst) or
                (self.board[1:10:4] == lst or self.board[2:7:2] == lst)):
            print(f'Победил {player}')
            return True


game = Game()
game.start_game()