import socket
from gameboard import *
import tkinter as tk

def getHostInfo():
    try:
        input_server = input("Enter the IP Address of Player 2:\n")
        input_port = int(input("Enter 6262 (Port Number) to play:\n"))
        createConnection(input_server, input_port)
    except ValueError:
        user_ans = input("Connection wasn't made. Try again? (Y/N)\n")
        if user_ans == 'y' or user_ans == 'Y':
            getHostInfo()

def createConnection(server, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    BoardClass.socket_obj = client_socket
    try:
        client_socket.connect((server,port))
        playTTT(client_socket)
    except ConnectionResetError:
        print("Host has closed the connection.")
    except ConnectionRefusedError or ValueError:
        user_ans = input("Connection wasn't made. Try again? (Y/N)\n")
        if user_ans == 'y' or user_ans == 'Y':
            getHostInfo()
        else:
            pass
    except tk.TclError or KeyError:
                print("Tic Tac Toe window closed.")

def playTTT(client_socket):
    print(client_socket.recv(1024).decode('ascii')) #confirm connection = 'Connection successful!'
    server_msg = client_socket.recv(1024).decode('ascii') #game starts or connection is closed
    
    if server_msg == 'Please send user name': #player 2 asks for name
        enterNames(client_socket) #name is entered and sent to player 2 module
        start_msg = client_socket.recv(1024).decode('ascii') #'Tic Tac Toe game start!'
        print(start_msg)
        BoardClass.colorTTTBoard(BoardClass)
        BoardClass.resetGameBoard(BoardClass) #first game is started
        ttt.update()
        
        game_active = True
        while game_active is True:
            
            if "Fun times!" in BoardClass.x_moves:
                print("Fun times!")
                client_socket.send(bytes('Fun times!', 'ascii'))
                BoardClass.printStats(BoardClass)
                ttt.update()
                game_active = False
                break
                
            if "Play again!" in BoardClass.x_moves:
                client_socket.send(bytes('Play again!', 'ascii'))
                BoardClass.resetGameBoard(BoardClass)
                ttt.update()
                continue
                
            if BoardClass.turn%2 == 0:
                ttt.update()
            
            if BoardClass.turn%2 == 1:
                client_socket.send(bytes('Your turn!', 'ascii'))
                p2_button = client_socket.recv(1024).decode()
                p2_button = globals()[p2_button]
                BoardClass.updateGameBoard(BoardClass, p2_button)
                ttt.update()
        
        client_socket.close()
    
    elif server_msg == 'Server is at maximum capacity!': #connection is closed
        print(server_msg)
        raise ConnectionResetError

def enterNames(client_socket):
    pu1 = BoardClass.user1_input.get()
    while pu1 == '':
        BoardClass.getPlayer1User(BoardClass)
        ttt.update()
        BoardClass.user1 = BoardClass.user1_input.get() #player 1 name entered in UI
        pu1 = BoardClass.user1 #player 1 name set
        BoardClass.MYNAME = pu1
        client_socket.send(bytes(pu1, 'ascii')) #player 1 name sent
    pu2 = client_socket.recv(1024).decode('ascii')
    BoardClass.user2 = pu2 #player 2 name received and set
    BoardClass.displayPlayer2Name(BoardClass)

if __name__ == '__main__':
    getHostInfo()
