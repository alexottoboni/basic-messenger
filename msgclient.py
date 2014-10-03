from Message import *
from socket import *   
import json

class MsgClient:

	def __init__(self, host = "127.0.0.1", port = 4446, mode = False):
		self.host = host
		self.port = port

		# True is sending mode, False is Recieving mode
		self.mode = mode   

	def send_msg(self):
	    target = raw_input("Who to send message to: ")
	    text = raw_input("Enter data: ")  
	    sender = socket.gethostname()
	    
	    print "Sender: ", sender 
	    
	    data = Message(sender, target, text)  
	    data = json.dumps(data)
	    s = socket(AF_INET, SOCK_STREAM)
	    s.connect((host,port))  
	    s.send(data)
	    msg = s.recv(512)
	    print "Message from server : " + msg
	    s.close()

	def get_msg(self):
		s = socket(AF_INET, SOCK_STREAM)
		s.bind((self.host, self.port))
		s.listen(1)
		print "Listening for message.. "
		
		new_socket, address = s.accept()
		data = new_socket.recv(512)

		got_msg = json.dumps(data)
		print "Message from: ", got_msg[Message.SENDER_KEY]
		print got_msg[Message.MESSAGE_KEY]
          
if __name__ == "__main__":
	
	mode = raw_input("Send or Get?: ")

	if mode.upper() == "SEND":
		host = raw_input("Server Address: ")
		client = MsgClient(host, 4446, True)
		client.send_msg()
	
	else:
		host = raw_input("My Local Address: ")
		client = MsgClient(host, 4446, False)
		client.get_msg()

	
