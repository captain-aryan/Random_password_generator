from main import Password

print(f'''[+] -l, Enters the lowercase list
[+] -u, Enters the uppercase list
[+] -n, Enters the numbers list
[+] -s, Enters the special characters list
''')
password = Password(input("Your CMD > "), int(input("Length of Password > ")))
password.set_the_charset()
password.generate_password()
print(password.get_password())