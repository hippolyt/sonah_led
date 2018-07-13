import socket


# Create and open a socket conection
# I switched the port to 8900, which resolved the connection refusal error
s = socket.socket()
s.connect(('192.168.1.2', 8900))

# function, which reads socket input
def receive():
    chunks =list()
    bytes_recd = 0
    while bytes_recd < 8:
        chunk = s.recv(min(8 - bytes_recd, 2048))
        if chunk == b'':
            print('hm')
    chunks.append(chunk)
    bytes_recd = bytes_recd + len(chunk)
    print( b''.join(chunks))

# Once you opened a socket connection to the controller, you need to transform
# the hex code to a bytearray. Fortunately, python comes with those batteries included:
hex_s = '$00 $00 $00 $00 $24 $01 $FE'.replace(' $', '').replace('$', '')
arr = bytearray.fromhex(hex_s)
s.send(arr)