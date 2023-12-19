import socket

# host = socket.gethostbyname(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '172.23.16.1'
PORT = 2525

server.bind((HOST, PORT))

server.listen(0)

# while True:
#     communication_socket, address = server.accept()
#     msg = communication_socket.recv(1024).decode("utf-8")
#     print(msg)
#     response = input("Response to the message: ")
#     communication_socket.send(response.encode("utf-8"))
    # communication_socket.close()


while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")

    while True:
        msg = communication_socket.recv(1024).decode("utf-8")
        if msg.lower() == "off":
            print("Client disconnected.")
            communication_socket.close()
            break
        print(f"Client message: {msg}")
        response = input("Response to the message(server): ")
        communication_socket.send(response.encode("utf-8"))

    