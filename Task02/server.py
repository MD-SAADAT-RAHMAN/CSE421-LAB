import socket


port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)


server_socket_address = (host_ip, port)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address) # attaches the socket to the chosen IP and port


server.listen() # puts the socket in listening mode
print("Server is listening")


buffer = 16
format = "utf-8"
disconnected = "End"


while True:
    conn, addr = server.accept() # waits client and creates a new connection socket, aikhane conn socket and addr hocche address of client
    print("Connected to", addr)
    connected = True


    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message is", message_length)


        if message_length: #  makes sure something was received
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(format)
            
            
            if msg == disconnected:
                conn.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating connection with", addr)
                connected = False
            else:
                # print(msg)
                # conn.send("I have received your message".encode(format))
                vowels = "aeiouAEIOU"
                total = 0
                for i in msg:
                    if i in vowels:
                        total += 1
                if total == 0:
                    conn.send("Not enough vowels".encode(format))
                elif total <= 2:
                    conn.send("Enough".encode(format))
                else:
                    conn.send("Too many".encode(format))


    conn.close()
