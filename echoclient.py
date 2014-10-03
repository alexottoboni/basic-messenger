# TCP Client Code
 
host="192.168.1.4"            # Set the server address to variable host
 
port=4446               # Sets the variable port to 4446
 
from socket import *             # Imports socket module
 
while 1:

    data = raw_input("Enter data: ")

    s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
             # Connect to server address
    s.connect((host,port))  

    s.send(data)
         
    msg=s.recv(512)            # Receives data upto 1024 bytes and stores in variables msg
         
    print "Message from server : " + msg
     
    s.close()                            # Closes the socket
    # End of code