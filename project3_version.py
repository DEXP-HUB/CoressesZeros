class Game:

    def create_game(self):
        self.players = (('x', 'x', 'x'), ('0', '0', '0'))
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def start_game(self):
       while True:
           if self.check_victory() is None:
               self.motion_players((self.check_lock_cell, player[0]))

    def motion_players(self, callback, player):
            print(f'Ходит {player[0]}')
            motion = input('Введите номер клетки: ')
            result = lambda x: (x == 1 and self.true_value()) or (self.motion_players(self.check_lock_cell, player[0]))
            print(result(callback(motion, player[0])))

    def false_value(self):
        return 'Ячейка занята, или вы ввели неверное значение.'

    def true_value(self):
        return f'{self.board[0:3]}\n{self.board[3:6]}\n{self.board[6:9]}'

    def check_lock_cell(self, motion, player):
        if motion.isdigit() and int(motion) <= 8:
            if self.board[int(motion)] == ' ':
                self.board[int(motion)] = player
                return 1
            else:
                print(self.false_value())
        else:
            return 0

    def check_victory(self):
        for player in self.players:
            if (self.board[0:3] == player or self.board[3:6] == player or self.board[6:9] == player) or \
                    (self.board[0:7:3] == player or self.board[1:8:3] == player or self.board[2:9:3] == player) or \
                    (self.board[0:9:4] == player or self.board[2:7:2] == player):
                return f'{player[0]} победил.'
            return None


game = Game()
game.create_game()
game.start_game()
