from socket import * 
from Message import *
import json

class MsgServer:

	def __init__(self, host = "127.0.0.1", port = 4446):
		self.connections = {}
		self.host = host
		self.port = port

	def start(self):
	    s = socket(AF_INET, SOCK_STREAM)
	    s.bind((self.host, self.port))
	    s.listen(1)
	    print "Listening for message.. "
		
	    new_socket, address = s.accept()
	    data = new_socket.recv(512)
	    new_msg = self.parse_msg(data)

	    if data:
		new_socket.send("Recieved Message")
	    s.close()

	    s = socket(AF_INET, SOCK_STREAM)
	    s.connect((new_msg[Message.RECIPIENT_KEY], self.port))  
	    s.send(json.dumps(new_msg))

	    s.close()


	def parse_msg(self, data):
		return json.loads(data)

	@staticmethod
	def get_my_ip():
		s = socket(AF_INET, SOCK_DGRAM) 
		s.connect(('8.8.8.8', 80)) 
		my_ip = (s.getsockname()[0]) 
		s.close()
		return my_ip

if __name__ == "__main__":
    my_ip = MsgServer.get_my_ip()
    server = MsgServer(str(my_ip), 4446)
    server.start()
