import socket
import threading


def client():
    IP = "192.168.8.198"
    PORT = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    name = input("What is your name: ")
    client_socket.send(name.encode("utf-8"))
    while True:
        threading.Thread(target=receive, args=(client_socket,)).start()
        msg = input("What would you like to say to the group: ")
        if msg == "off":
            client_socket.close()
            break
        client_socket.send(msg.encode("utf-8"))
        
def receive(client_socket):
    msg = client_socket.recv(1024).decode("utf-8")
    print(f"\nmessage from {msg}\nwhat would you like to say to group: ", end = "")

client()