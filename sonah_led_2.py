import socket
from array import array
from time import sleep
import random
import codecs

ROW = []
ROW.append('$00 $00 $00 $00 $24 $0')
ROW.append('$FE')

NUMBER = []
NUMBER.append('$00 $00 $00 $00 $01 $02 $57 $30 $30 $00 $00 $00 $32 $FD $07 $06 $00 $00 $00')
NUMBER.append('$9')
NUMBER.append('$FE')

IP = '10.1.0.104'
PORT = 8900

# Create and open a socket conection
# I switched the port to 8900, which resolved the connection refusal error
s = socket.socket()
s.connect((IP, PORT))

def receive():
    sleep(0.3)
    response = s.recv(2048)
    print('Response: ' + str(response))

# function, which reads socket input
def receive2():
    chunks =list()
    bytes_recd = 0
    while bytes_recd < 8:
        chunk = s.recv(min(8 - bytes_recd, 2048))
        if chunk == b'':
            print('hm')
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    print('Response: ' + str(b''.join(chunks)))

def to_hex(input):
    hex_result = format(ord(input), "x")
    # hex_result = codecs.encode(chr(input), "hex")
    # = str(str(input).encode("hex"))
    return hex_result

def show_text(input):
    text = str(input)
    text = text.ljust(12)
    show(1, text[0], text[1], text[2])
    show(2, text[3], text[4], text[5])
    show(3, text[6], text[7], text[8])
    show(4, text[9], text[10], text[11])


def show_row(row_index, input):
    text = str(input)
    text = text.ljust(3)
    show(row_index, text[0], text[1], text[2])


def show(row_index, char1, char2, char3):
    # Choose ROW
    send(ROW[0] + str(row_index) + ROW[1])
    # Show text
    string = NUMBER[0] +  to_hex(char1) + to_hex(char2) + to_hex(char3) + NUMBER[2]
    print('HEX command: ' + string)
    send(string)

def send(hexCmd):
    hex_s = hexCmd.replace(' $', '').replace('$', '')
    print('cleaned HEX command: ' + str(hex_s))
    arr = bytearray.fromhex(hex_s)
    print('bytearray: ' + str(arr))
    s.send(arr)
    receive()

def exit_message():
    input("You have not chosen a valid option. Press Enter to exit.")
    exit()

mode = input("Do you want to write to \n (1) a row \n (2) the whole sign?\n")
if (mode == "1"):
    row = input("Which row you want to show text on? [1 - 4]\n")
    if (row == "1" or row == "2" or row == "3" or row == "4"):
        text = input("What text would you like to show? (Just the first 3 digits will be shown) \n")
        show_row(row, text)
    else:
        exit_message()
elif(mode == "2"):
    text = input("What text should the LED Sign show?\n")
    show_text(text)
elif(mode == "3"):
    hexCommand = "00000040010257303000000032FD0706000000919233FE"
    send(hexCommand)
else:
    exit_message()
