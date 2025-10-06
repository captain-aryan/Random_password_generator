import string
import random

class Password:

    def __init__(self, charset, length):
        self.charset = charset
        self.length = length
        self.char_array = []

    def set_the_charset(self):
        if ('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)

        elif ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)

        elif ('d' in self.charset):
            self.char_array.append(string.digits)

        elif ('s' in self.charset):
            self.char_array.append(string.punctuation)
    
    def get_char_array(self):
    
        return self.char_array
    
    def generate_password(self):
        