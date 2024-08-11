class Game:
    #Функция в которой начинаеться игра.
    def start_game(self):
        self.player1 = 'x'
        self.player2 = '0'

        #создание игрового поля.
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

        #Цикл для запуска постоянной проверки победителя, и метода
        # motion_players, для передачи в него игрока который ходит.
        while True:
            if self.user_victory():
                print(self.user_victory())
                break
            self.motion_players(self.player1)
            if self.user_victory():
                print(self.user_victory())
                break
            self.motion_players(self.player2)
            if self.user_victory():
                print(self.user_victory())
                break
    # Функция выполняет ходы пользователей, и проверяет какая ячейка занята, если ячейка занята,
    # то выводится сообщение: 'Эта ячейка уже занята.', а так же проверяеться вероятные ошибки в try, и except.
    def motion_players(self, player):
        try:
            print(f'Ходит {player}')
            motion = int(input('Введите номер клетки: '))
            if self.board[motion] == ' ':
                self.board[motion] = player
                print(self.board[0:3], self.board[3:6], self.board[6:9], sep='\n')
            else:
                print('Эта ячейка уже занята.')
                self.motion_players(player)
        except (ValueError, IndexError):
            print('Ошибка')
            self.motion_players(player)
    #Функция для проверки победителя, она же, и вызывается в методе start_game.
    def user_victory(self):
        if (self.board[0] == 'x' and self.board[1] == 'x' and self.board[2] == 'x') or \
                (self.board[3] == 'x' and self.board[4] == 'x' and self.board[5] == 'x') or \
                (self.board[6] == 'x' and self.board[7] == 'x' and self.board[8] == 'x') or \
                (self.board[0] == 'x' and self.board[3] == 'x' and self.board[6] == 'x') or \
                (self.board[1] == 'x' and self.board[4] == 'x' and self.board[7] == 'x') or \
                (self.board[2] == 'x' and self.board[5] == 'x' and self.board[8] == 'x') or \
                (self.board[0] == 'x' and self.board[4] == 'x' and self.board[8] == 'x') or \
                (self.board[2] == 'x' and self.board[4] == 'x' and self.board[6] == 'x'):
            return f'{self.player1} победил!'
        elif (self.board[0] == '0' and self.board[1] == '0' and self.board[2] == '0') or \
                (self.board[3] == '0' and self.board[4] == '0' and self.board[5] == '0') or \
                (self.board[6] == '0' and self.board[7] == '0' and self.board[8] == '0') or \
                (self.board[0] == '0' and self.board[3] == '0' and self.board[6] == '0') or \
                (self.board[1] == '0' and self.board[4] == '0' and self.board[7] == '0') or \
                (self.board[2] == '0' and self.board[5] == '0' and self.board[8] == '0') or \
                (self.board[0] == '0' and self.board[4] == '0' and self.board[8] == '0') or \
                (self.board[2] == '0' and self.board[4] == '0' and self.board[6] == '0'):
            return f'{self.player2} победил!'
        else:
            return None


game = Game()
game.start_game()
