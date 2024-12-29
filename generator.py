# Generate your password
import random
import pyperclip

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'X']
dig = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sym = ['!', '$', '%', '&', '*', '-', '?']

all_symbols = [abc, ABC, dig, sym]
password = ''

for i in range(15):
    s = random.choice(all_symbols)
    password_s = random.choice(s)
    s.remove(password_s)
    password += password_s

print(f'Password: {password}')
pyperclip.copy(password)
print('Your password has been copied to the clipboard')
