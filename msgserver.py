# TCP Server Code
 
host="192.168.1.4"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4446
from socket import *                # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)
 
s.bind((host,port))                 # Binds the socket. Note that the input to
                                            # the bind function is a tuple
 
                      # Sets socket to listening state with a  queue
                                            # of 5 connection

print "Listening for connections.. "

s.listen(1)  

while(1): 
     
    q,addr=s.accept()   
    data = q.recv(1024)   

    if data:       
        print addr, data
        q.send(data)                      
 
s.close()
 
# End of code