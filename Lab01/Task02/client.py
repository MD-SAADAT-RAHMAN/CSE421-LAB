import socket


port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname) # convert hostname to IPv4 address into string format


server_socket_address = (host_ip, port) # create a tuple of the server socket address as its using server port number

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object for the client using IPv4 and TCP protocol
client.connect(server_socket_address) #connects the client to the server



format = "utf-8"
buffer = 16
disconnected = "End"


def msg_to_be_sent(msg):
    message = msg.encode(format) # converts text into bytes
    msg_length = len(message) # counts how many bytes the message has
    msg_length = str(msg_length).encode(format)
    msg_length += b" " * (buffer-len(msg_length))


    client.send(msg_length)
    client.send(message)


    print(client.recv(2048).decode(format))


# msg_to_be_sent(f"IP address of the client is {host_ip} and the device name is {hostname}")
# msg_to_be_sent(disconnected)


while True:
    inpt = input("Enter something ")
    if inpt == "Done":
        msg_to_be_sent(disconnected)
        break
    else:
        msg_to_be_sent(inpt)

