import socket

# Initialize Socket Instance 
soc = socket.socket()
print ("Socket has been created successfully.")

# Defining configurations for port and host
host = "127.0.0.1"
port = 60001

#Binding to the client connection
soc.bind((host, port))

# Accepts up to 20 connections
soc.listen(5)
print('Socket is listening...')

while True:
    # Establish the connection with the clients.
    connection, addr = soc.accept()
    print('Connected has been established with ', addr)

    # Receiving data from client
    dataFile = connection.recv(1024)

    # File info
    fileName = 'demofile.txt'
    file = open(fileName, 'rb')
    line = file.read(1024)

    # Keep sending data to the client
    while(line):
        connection.send(line)
        line = file.read(1024)
    
    #closing the file after sending successfully
    file.close()
    print('File has been sent to the client successfully.')

    connection.close()
