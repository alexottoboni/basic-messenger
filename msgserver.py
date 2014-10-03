from socket import * 
from Message import *
import json

class MsgServer:

    def __init__(self, host = "127.0.0.1", port = 4446):
        self.connections = {}
        self.host = host
        self.port = port

    def start(self):
        """
            Starts the server to route messages
        """
        # Creates new socket to listen to
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)
        print "Listening for message.. "
        
        # Process a new message
        new_socket, address = s.accept()
        data = new_socket.recv(512)
        new_msg = self.parse_msg(data)

        if data:
            new_socket.send("Recieved Message")
            s.close()

        s = socket(AF_INET, SOCK_STREAM)
        s.connect((new_msg[Message.RECIPIENT_KEY], self.port))
        new_msg = self.package_msg(new_msg)  
        s.send(new_msg)

        s.close()

    def parse_msg(self, data):
        """
            Takes JSON string and turns into a dictionary

            @data: The JSON formatted string
        """
        return json.loads(data)

    def package_msg(self, data):
        """
            Takes a dictionary and dumps it as a JSON string

            @data: The python dictionary
        """
        return json.dumps(data)

if __name__ == "__main__":
    my_ip = MsgServer.get_my_ip()
    server = MsgServer(str(my_ip), 4446)
    server.start()
