import pyqrcode

txt = input("Input text or link for generating the QR Code: ")

qr = pyqrcode.create(txt)

option = input('''
How do you want the output?

    1) PNG
    2) SVG
    3) Terminal

1, 2 or 3?: ''')

if option == '1':
    qr.png('qr.png', scale=10)
elif option == '2':
    qr.svg('qr.svg', scale=10)
elif option == '3':
    print(qr.terminal())
else:
    print("You chose a wrong answer, ending...")