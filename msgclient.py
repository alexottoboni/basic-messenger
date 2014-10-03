from Message import *
from socket import *  
from NetworkUtilities import * 
import json

class MsgClient:

	def __init__(self, host = "127.0.0.1", port = 4446, mode = False):
		"""
			Creates a new client for sending and recieving messages based on
			what mode it is in. 

			@host: The server address to connect to. If in get mode this is 
			itself 

			@port: The port to establish the connection on

			@mode: The mode the client is in, either sending or getting messages
		"""
		self.host = host
		self.port = port

		# True is sending mode, False is Recieving mode
		self.mode = mode  

	def send_msg(self, target, data):
		"""
			Sends a message to a computer

			@target: The ip address of the computer we are sending
					 the message to. This should be a string

			@data: The data we are sending, usually the string representation
				   of JSON. 
		"""
		# Get IP Address to populate message sender field
		my_addr = NetworkUtilities.get_my_ip()

		# Create a new message object	    
	    msg = Message(my_addr, target, data)  
	    msg = msg.get_json()
	    
	    # Create a new connection to the server
	    s = socket(AF_INET, SOCK_STREAM)
	    s.connect((self.host, self.port))  
	    s.send(msg)

	    # Get response from server
	    response = s.recv(512)
	    print "Response from server : " + response
	    s.close()

	def get_msg(self):
		"""
			Method that lets the client listen for a new message
		"""
		# Create a new connection to the server
		s = socket(AF_INET, SOCK_STREAM)
		s.bind((self.host, self.port))
		s.listen(1)
		print "Listening for message.. "
		
		# Get message from server
		new_socket, address = s.accept()
		data = new_socket.recv(512)
		recieved_msg = json.loads(data)
		print "Message from: ", recieved_msg[Message.SENDER_KEY]
		print got_msg[Message.MESSAGE_KEY]
          
if __name__ == "__main__":
	
	mode = raw_input("Send or Get?: ")

	if mode.upper() == "SEND":
		host = raw_input("Server Address: ")
		target = raw_input("Who to send message to: ")
		text = raw_input("Enter data: ")  
		client = MsgClient(host, 4446, True)
		client.send_msg(target, text)
	
	elif mode.upper() == "GET":
		my_ip = NetworkUtilities.get_my_ip()
		client = MsgClient(my_ip, 4446, False)
		client.get_msg()
	
	else:
		raise ValueError("Invalid Mode, must be Get or Send")

	
