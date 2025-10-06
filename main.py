import string
import random
import argparse

argparse = argparse.ArgumentParser(description="Random Password Generator", usage="python3 pass_gen.py -l LOWERCASE -u UPPERCASE -d NUMERIC -s SPECIAL_CHAR")
argparse.add_argument("-l","--lowercase",help="Enters the lowercase list")
argparse.add_argument("-u","--uppercase",help="Enters the uppercase list")
argparse.add_argument("-d","--numeric",help="Enters the numbers list")
argparse.add_argument("-s","--special",help="Enters the special characters list")

args = argparse.parse_args()
lowercase = args.lowercase
uppercase = args.uppercase
numbers = args.numbers
special_char = args.special_char

print(f"[+] ")

class Password:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length
        self.char_array = []
        self.password = []

    def set_the_charset(self):
        if ('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)

        if ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)

        if ('d' in self.charset):
            self.char_array.append(string.digits)

        if ('s' in self.charset):
            self.char_array.append(string.punctuation)
    
    def get_char_array(self):
    
        return self.char_array
    
    def generate_password(self):
        print(self.char_array)
        for i in range(len(self.length)):
            outer_index = random.randrange(0, len(self.char_array))
            inner_index = random.randrange(0, len(self.char_array[outer_index]))
            self.password.append(self.char_array[outer_index] [inner_index])
