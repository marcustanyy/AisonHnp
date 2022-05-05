import socket

def Connect_server(server):
    TCP_IP = socket.gethostname()
    TCP_PORT = 8000
    BUFFER_SIZE = 1024
    MESSAGE = "update"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, TCP_PORT))
    server.send(MESSAGE.encode())
    data = server.recv(BUFFER_SIZE)
    # s.close()
    print("received data:", data.decode())

def Close_connection(server):
    server.close()
    print("Closed connection.")
    
def Send_data(server, data):
    server.send(data.encode())

server = socket.socket()
Connect_server(server)
