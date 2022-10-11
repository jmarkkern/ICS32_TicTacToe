import socket, pickle
from gameboard import *
import tkinter as tk

def makeServer():
    ttt_port = 6262

    #create server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', ttt_port))
    createConnection(server_socket)

def createConnection(server_socket):
    server_socket.listen(1)
    print("Server waiting for connection...")
    connect_count = 0
    running = True

    while running is True:
        #accept client connection
        client_socket, client_address = server_socket.accept()
        print("Player connected from "+client_address[0])
        client_socket.send(b'Connection successful!') #confirm connection
        connect_count += 1
        if connect_count == 2:
            running = False
            client_socket.send(b'Server is at maximum capacity! Try again later...')
            server_socket.close()
        else:
            try:
                playTTT(client_socket)
            except ConnectionResetError:
                print("Player has closed connection.")
            except tk.TclError:
                print("Tic Tac Toe window closed.")
                client_socket.close()
                

def playTTT(client_socket):
    BoardClass.socket_obj = client_socket
    client_socket.send(b'Please send user name')
    print("Waiting for Player 1 to send user name...")
    retrieveNames(client_socket) #get names
    client_socket.send(b'Tic Tac Toe game start!') #names are displayed on ui
    print('Tic Tac Toe game start!')
    BoardClass.colorTTTBoard(BoardClass)
    BoardClass.resetGameBoard(BoardClass) #start game
    ttt.update()

    game_active = True
    while game_active is True:
        p1_cmd = client_socket.recv(1024).decode()
        
        if p1_cmd == 'Fun times!':
            print(p1_cmd)
            BoardClass.printStats(BoardClass)
            ttt.update()
            game_active = False
            break
        
        if p1_cmd == 'Play again!':
            BoardClass.resetGameBoard(BoardClass)
            ttt.update()
            continue
        
        if p1_cmd == 'Your turn!':
            while BoardClass.turn%2 == 1:
                ttt.update()
            continue
        
        if BoardClass.turn%2 == 0:
            p1_button = globals()[p1_cmd]
            BoardClass.updateGameBoard(BoardClass, p1_button)
            ttt.update()

    client_socket.close()

def retrieveNames(client_socket):
    pu1 = client_socket.recv(1024).decode('ascii')
    BoardClass.user1 = pu1 #player 1 name received and set
    BoardClass.displayPlayer1Name(BoardClass)
    BoardClass.user2 = 'Player 2' #player 2 name set
    BoardClass.MYNAME = BoardClass.user2
    BoardClass.displayPlayer2Name(BoardClass)
    ttt.update()
    client_socket.send(bytes(BoardClass.user2, 'ascii')) #player 2 name sent

if __name__ == '__main__':
    makeServer()
