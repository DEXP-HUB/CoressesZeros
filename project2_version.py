class Game:

    def create_game(self):
        self.player1 = 'x'
        self.player2 = '0'
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def start_game(self):
        self.create_game()
        for i in range(len(self.board)):
            if self.player_victory((self.player1, self.player2)) == False:
                self.motion_players((self.player1, self.player2))
            else:
                print('Игра окончена')

    def motion_players(self, players):
        for player in players:
            try:
                print(f'Ходит {player}')
                motion = int(input('Введите номер клетки: '))
                if self.board[motion] == ' ':
                    self.board[motion] = player
                    print(self.board[0:3], self.board[3:6], self.board[6:9], sep='\n')
                else:
                    print('Эта ячейка уже занята.')
            except (ValueError, IndexError):
                    print('Ошибка.')

    def player_victory(self, players):
        for player in players:
            if self.check_victory(player):
                return True
            return False

    def check_victory(self, players):
        for player in players:
            if (self.board[0:3] == player or self.board[3:6] == player or self.board[6:9] == player) or \
                    (self.board[0:7:3] == player or self.board[1:8:3] == player or self.board[2:9:3] == player) or \
                    (self.board[0:9:4] == player or self.board[2:7:2] == player):
                return f'{player} Победил.'




