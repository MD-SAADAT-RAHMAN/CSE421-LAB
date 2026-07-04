import socket
import threading


port = 5050
hostname = socket.gethostname()
host_ip = socket.gethostbyname(hostname)


server_socket_address = (host_ip, port)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_socket_address)


server.listen()
print("Server is listening")

port = 5050
buffer = 16
format = "utf-8"
disconnected = "End"


def handle_clients(conn, addr):
    # conn, addr = server.accept()
    print("Connected to", addr)
    connected = True


    while connected:
        message_length = conn.recv(buffer).decode(format)
        print("Length of the message is", message_length)


        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(format)
            
            
            if msg == disconnected:
                conn.send("Goodbye. It was nice to serve you.".encode(format))
                print("Terminating connection with", addr)
                connected = False
            else:
                # print(msg)
                # conn.send("I have received your message".encode(format))
                number = int(msg)
                
                if number <= 40 and number >= 0:
                    salary = number * 200
                    
                else:
                    salary = 8000 + (number - 40) * 300
                    
                conn.send(f"Your salary is Tk {salary}".encode(format))

    conn.close()
    print("Connection closed with", addr)

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target = handle_clients, args = (conn, addr))
    thread.start()
