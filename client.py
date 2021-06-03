import socket

# Initialize Socket Instance
soc = socket.socket()
print ("Socket created successfully.")

# Defining port and host configurations and establishing connection
host = "127.0.0.1"
port = 60001
soc.connect((host, port))
print('Connection has been Established.')

# Sending message to server
soc.send('Hi there, Knock Knock from client'.encode())

# Write File in binary
file = open('client.txt', 'wb')
line = soc.recv(1024)

while(line):
    file.write(line)
    line = soc.recv(1024)

print('File has been received successfully.')

#closing the connection and file
file.close()
soc.close()
print('Connection Closed.')
