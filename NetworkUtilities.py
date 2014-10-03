from socket import *

class NetworkUtilities:

    @staticmethod
    def get_my_ip():
        """
            Simple method to get the local ip address of the current machine
        """
        s = socket(AF_INET, SOCK_DGRAM) # Opens socket
        s.connect(('8.8.8.8', 80)) # Connects to Google's DNS
        my_ip = (s.getsockname()[0]) # Gets our IP Address
        s.close() 
        return my_ip