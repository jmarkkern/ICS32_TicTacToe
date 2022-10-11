import tkinter as tk
from tkinter import messagebox

class BoardClass():

    ttt = ''
    socket_obj = ''
    MYNAME = ''
    
    turn = 0
    current_user = ''
    last_user = ''
    num_games = 0
    num_ties = 0

    user1_input = ''
    user1 = ''
    x_moves = []
    x_wins = 0
    x_losses = 0
    
    user2 = ''
    o_wins = 0
    o_losses = 0
    
    def getPlayer1User(self):
        self.user1_entry = tk.Entry(self.ttt, textvariable=self.user1_input, width=15)
        self.user1_entry.grid(row=2, column=1)

    def displayPlayer1Name(self):
        self.user1_lbl = tk.Label(self.ttt, text=self.user1, height=1, width=15, bg='white', anchor='w')
        self.user1_lbl.grid(row=2, column=1)

    def displayPlayer2Name(self):
        self.user2_lbl = tk.Label(self.ttt, text=self.user2, height=1, width=15, bg='white', anchor='w')
        self.user2_lbl.grid(row=2, column=2)

    def colorTTTBoard(self):
        if self.MYNAME == self.user1:
            ttt['bg'] = '#D4F2B7'
        if self.MYNAME == self.user2:
            ttt['bg'] = '#F2B7B7'

    def updateCurrentPlayer(self):
        if self.turn%2 == 0:
            self.current_user = self.user1
            self.last_user = self.user1
        else:
            self.current_user = self.user2
            self.last_user = self.user2
        current_user_lbl = tk.Label(self.ttt, text=self.current_user, height=1, width=15, bg='white', anchor='w')
        current_user_lbl.grid(row=2, column=3)

    def updateGamesPlayed(self):
        BoardClass.num_games += 1

    def updateGameBoard(self, button):
        if self.turn%2 == 0:
            if button['text'] == '':
                button['text'] = 'X'
                button['bg'] = '#B5EB7E'
                self.x_moves.append(button)
                if BoardClass.isWinner(self) == False:
                    if BoardClass.boardIsFull(self) == False:
                        self.turn += 1
            else:
                tk.messagebox.showwarning('Tic Tac Toe', 'Choose another box!')
        
        else:
            if button['text'] == '':
                button['text'] = 'O'
                button['bg'] = '#EB7E7E'
                if BoardClass.isWinner(self) == False:
                    if BoardClass.boardIsFull(self) == False:
                        self.turn += 1
            else:
                tk.messagebox.showwarning('Tic Tac Toe', 'Choose another box!')
        BoardClass.updateCurrentPlayer(self)

    def isWinner(self):
        if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
            BoardClass.x_wins += 1
            BoardClass.o_losses += 1
            tk.messagebox.showinfo('Tic Tac Toe', self.user1+' wins!')
            if self.MYNAME == self.user1:
                BoardClass.playAgainAsk(BoardClass)
            elif self.MYNAME == self.user2:
                self.turn += 1
            return True
            
        elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
              button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
              button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
              button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
              button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
              button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
              button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
              button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
            BoardClass.o_wins += 1
            BoardClass.x_losses += 1
            tk.messagebox.showinfo('Tic Tac Toe', self.user2+' wins!')
            if self.MYNAME == self.user1:
                BoardClass.playAgainAsk(BoardClass)
            elif self.MYNAME == self.user2:
                self.turn += 1
            return True

        else:
            return False

    def boardIsFull(self):
        board_space = []
        for button in buttons:
            board_space.append(button['text'])
        if '' not in board_space:
            BoardClass.num_ties += 1
            tk.messagebox.showinfo('Tic Tac Toe', 'Game was tied!')
            if self.MYNAME == self.user1:
                BoardClass.playAgainAsk(BoardClass)
            elif self.MYNAME == self.user2:
                self.turn += 1
            return True
        else:
            return False

    def playAgainAsk(self):
        if tk.messagebox.askyesno('Tic Tac Toe', 'Would you like to play again?'):
            self.x_moves.append("Play again!")
        else:
            self.x_moves.append("Fun times!")

    def printStats(self):
        for button in buttons:
            button['text'] = 'GG'
        stats = ''
        if self.MYNAME == self.user1:
            stats += 'Player: '+self.user1
            stats += '\nLast Move: '+self.last_user
            stats += '\nGames Played: '+str(self.num_games)
            stats += '\nGames Won: '+str(self.x_wins)
            stats += '\nGames Lost: '+str(self.x_losses)
            stats += '\nGames Tied: '+str(self.num_ties)
            self.stats_label = tk.Label(self.ttt, text=stats, bg='#B5EB7E', height=6, width=15)
            self.stats_label.grid(row=4, column=4)
        if self.MYNAME == self.user2:
            stats += 'Player: '+self.user2
            stats += '\nLast Move: '+self.last_user
            stats += '\nGames Played: '+str(self.num_games)
            stats += '\nGames Won: '+str(self.o_wins)
            stats += '\nGames Lost: '+str(self.o_losses)
            stats += '\nGames Tied: '+str(self.num_ties)
            self.stats_label = tk.Label(self.ttt, text=stats, bg='#EB7E7E', height=6, width=15)
            self.stats_label.grid(row=4, column=4)

    def resetGameBoard(self):
        BoardClass.updateGamesPlayed(self)
        self.turn = 0
        self.x_moves = []
        self.o_moves = []
        BoardClass.updateCurrentPlayer(self)
        for button in buttons:
            button['text'] = ''
            button['bg'] = 'gray'

def sendButton(socket_obj, button):
    button_name = [k for k,v in globals().items() if v == button][0]
    BoardClass.socket_obj.send(button_name.encode())

ttt = tk.Tk()
ttt.title("Tic Tac Toe")

u1_label = tk.Label(ttt, text="Player 1:", height=1, width=15, bg='white', anchor='w')
u1_label.grid(row=1, column=1)
BoardClass.user1_input = tk.StringVar()

u2_label = tk.Label(ttt, text="Player 2:", height=1, width=15, bg='white', anchor='w')
u2_label.grid(row=1, column=2)

current_move_lbl = tk.Label(ttt, text="Current Move:", height=1, width=15, bg='white', anchor='w')
current_move_lbl.grid(row=1, column=3)

quit_button = tk.Button(ttt, text="Quit Tic Tac Toe", height=1, width=15, command=lambda:ttt.destroy())
quit_button.grid(row=2, column=4)

button1 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button1),sendButton(BoardClass.socket_obj, button1)])
button1.grid(row=4, column=1)

button2 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button2),sendButton(BoardClass.socket_obj, button2)])
button2.grid(row=4, column=2)

button3 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button3),sendButton(BoardClass.socket_obj, button3)])
button3.grid(row=4, column=3)

button4 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button4),sendButton(BoardClass.socket_obj, button4)])
button4.grid(row=5, column=1)

button5 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button5),sendButton(BoardClass.socket_obj, button5)])
button5.grid(row=5, column=2)

button6 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button6),sendButton(BoardClass.socket_obj, button6)])
button6.grid(row=5, column=3)

button7 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button7),sendButton(BoardClass.socket_obj, button7)])
button7.grid(row=6, column=1)

button8 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button8),sendButton(BoardClass.socket_obj, button8)])
button8.grid(row=6, column=2)

button9 = tk.Button(ttt, height=6, width=15, text="X/O", command=lambda:[BoardClass.updateGameBoard(BoardClass, button9),sendButton(BoardClass.socket_obj, button9)])
button9.grid(row=6, column=3)

buttons = [button1,button2,button3,button4,button5,button6,button7,button8,button9]
