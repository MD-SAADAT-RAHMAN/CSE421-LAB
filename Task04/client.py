import socket


port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)


server_socket_address = (host_ip, port)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_address)



format = "utf-8"
buffer = 16
disconnected = "End"


def msg_to_be_sent(msg):
    message = msg.encode(format) # converts text into bytes
    msg_length = len(message) # counts how many bytes the message has
    msg_length = str(msg_length).encode(format) # converts the number into text, then into bytes as for encoding msg needs to be in string and then into bytes for sending it to the server
    msg_length += b" " * (buffer-len(msg_length)) # pads spaces to right so msg becomes 16 bytes long as server aitai chacche


    client.send(msg_length) #  sends the message length first
    client.send(message) # : sends the real message.


    print(client.recv(2048).decode(format)) # server er msg receive kore decode kore print korbe


# msg_to_be_sent(f"IP address of the client is {host_ip} and the device name is {hostname}")
# msg_to_be_sent(disconnected)


while True:
    inpt = input("Enter number of hours worked: ")
    if inpt == "Done":
        msg_to_be_sent(disconnected)
        break
    else:
        msg_to_be_sent(inpt)

