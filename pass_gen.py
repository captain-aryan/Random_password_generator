from main import Password
import argparse

args = argparse.ArgumentParser('''[+] l, Enters the lowercase password
       [+] u, Enters the uppercase password
       [+] n, Enters the numbers password
       [+] s, Enters the special characters password
''')
args.add_argument('-c','--charset', required=True)
args.add_argument('-l','--length', required=True)
options = args.parse_args()
print(options.charset)
print(options.length)

password = Password(options.charset, int(options.length))
password.set_the_charset()
password.generate_password()
print("Random Password is:",password.get_password())