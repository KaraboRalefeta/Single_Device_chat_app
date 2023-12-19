import socket

# host = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '172.23.16.1'
PORT = 2525


client.connect((HOST, PORT))

while True:
    msg = input("Message (client): ")
    client.send(msg.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    if not response:
        print("Server closed the connection.")
        client.close()
        break
    print(f"Server message: {response}")