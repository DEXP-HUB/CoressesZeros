class Game:

    def create_game(self):
        self.player1 = 'x'
        self.player2 = '0'
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def start_game(self):
        self.create_game()
        for move in range(len(self.board)):
            self.motion_players(self.player1)
            if self.user_victory(self.player1):
                print('Победил X')
                break
            self.motion_players(self.player2)
            if self.user_victory(self.player2):
                print('Победил 0')
                break

    def motion_players(self, player):
        while True:
            try:
                print(f'Ходит {player}')
                motion = int(input('Введите номер клетки: '))
                if self.board[motion] == ' ':
                    self.board[motion] = player
                    print(self.board[0:3], self.board[3:6], self.board[6:9], sep='\n')
                    break
                else:
                    print('Эта ячейка уже занята.')
            except (ValueError, IndexError):
                    print('Ошибка.')

    def user_victory(self, player):
        lst = [player, player, player]
        if (self.board[0:3] == lst or self.board[3:6] == lst or self.board[6:9] == lst) or \
                (self.board[0:7:3] == lst or self.board[1:8:3] == lst or self.board[2:9:3] == lst) or \
                (self.board[0:9:4] == lst or self.board[2:7:2] == lst):
            return f'{player} Победил.'


game = Game()
game.start_game()

