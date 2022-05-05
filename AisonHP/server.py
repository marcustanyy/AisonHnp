import socket, json

server = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8000                # Reserve a port for your service.
server.bind((host, port))        # Bind to the port
buffer = 1024

machine_status = {"temp" : "30 °C", "status" : "IDLE"}

server.listen(5)                 # Now wait for client connection.
inputs = [server]
outputs = []
messages = []
while inputs:
    con, addr = server.accept()     # Establish connection with client.
    inputs.append(con)
    print('Got connection from', addr)
    packet = con.recv(buffer)
    data = packet.decode()
    if data != "update":
        machine_status["status"] = packet.decode()  
    con.send(json.dumps(machine_status).encode())
    con.close()                # Close the connection

        