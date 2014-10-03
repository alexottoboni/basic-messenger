import json

class Message:

	SENDER_KEY = "sender"
	RECIPIENT_KEY = "recipient"
	MESSAGE_KEY = "msg"

	def __init__(self, sender = None, recipient = None, message = None):
		"""
			Creates a new message object
			@sender: The address of the computer sending the message
			@recipient: The address of the computer recieving the message
			@message: The contents of the message being sent
		"""
		self.data = {}
		self.data[SENDER_KEY] = sender
		self.data[RECIPIENT_KEY] = recipient
		self.data[MESSAGE_KEY] = message

	def get_json(self):
		return json.dumps(self.data)

	def is_json_valid(self, json_dict):
		keys_in_json = json_dict.keys()
		has_only_three_keys = (len(keys_in_json) == 3)

		if (SENDER_KEY in keys_in_json) and (RECIPIENT_KEY in keys_in_json) and (MESSAGE_KEY in keys_in_json):
			has_correct_keys = True
		else:
			has_correct_keys = False

		return has_correct_keys and has_only_three_keys

	def set_from_json(self, json_str):
		json_dict = json_str.loads(json_str)
		is_valid = self.is_json_valid(json_dict)

		if is_valid:  
			self.data = json_dict

