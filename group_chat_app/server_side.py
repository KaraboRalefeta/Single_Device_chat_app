import socket
import threading

def server_socket():
    people = dict()

    IP = "192.168.8.199"
    PORT = 123456

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((IP, PORT))

    server.listen(0)

    while True:
        new_sock, address = server.accept()
        name = new_sock.recv(1024).decode("utf-8")
        people[new_sock] = name
        thread = threading.Thread(target=handle_client, args = (people, new_sock, server))
        thread.start()

        pass



def handle_client(people, new_sock, server):
    while True:
        msg = new_sock.recv(1024).decode("utf-8")
        delete = False
        for i in people:
            if msg == "off":
                if i == new_sock:
                    delete = True
                else:
                    i.send(f"{people[new_sock]} has left the room".encode("utf-8"))
            elif i != new_sock:
                i.send(f"{people[new_sock]}: {msg}".encode("utf-8"))
        if delete:
            new_sock.close()
            del people[new_sock]
            if len(people) == 0:
                server.closer()
                break
server_socket()