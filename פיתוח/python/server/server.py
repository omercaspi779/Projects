import socket
from _thread import *

server = "192.168.56.1"
port = 9090
connections = 0
clients_play = 0
client_list = []
client_data = {}
clients_play_list = []
current_attack = 0
attack_sender = ""
target_user = ""
turn = 0
turns = 0
turn_name = ""
client_ip = 0
clients_play_ip = []
connected_usernames = []
global target_ip
target_ip = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("[+] Server Listening....")
print(socket.gethostbyname(socket.gethostname()))


def send_to_all_clients(message):
    for connection in client_list:
        try:
            connection.send(str.encode(f"{message},{','.join(connected_usernames)}"))
        except:
            pass


def threaded_client(connection):
    global connections, clients_play, current_attack, attack_sender, client_list, target_user, turn, turn_name, turns, client_ip, target_ip, clients_play_ip, connected_usernames
    username = ""
    connection.send(str.encode("Please provide a username or identifier"))
    try:
        username = connection.recv(2048).decode().strip()
        if username in connected_usernames:
            connection.send(str.encode("Username already connected. Please choose a different username."))
            connection.close()
            return
        connected_usernames.append(username)
        client_data[username] = connection
    except:
        pass
    message = f"{connections},{clients_play},{current_attack},{attack_sender},{target_user},{username},{turn_name},{target_ip}"
    send_to_all_clients(message)
    while True:
        try:
            data = connection.recv(2048).decode()
            if not data:
                print(f"[+] Disconnected: {username}")
                break
            else:
                print(f"Received from {username}: {data}")
            if data == "play":
                clients_play += 1
                clients_play_list.append(username)
                clients_play_ip.append(client_ip)
                print(f"{username} start play")
            elif data == "back":
                if clients_play > 0:
                    clients_play -= 1
                    if username in clients_play_list:
                        clients_play_list.remove(username)
                        clients_play_ip.remove(client_ip)
                    print(f"{username} stop play")
            elif data == "done":
                turns += 1
            elif data == "disconnect":
                if username in connected_usernames:
                    connected_usernames.remove(username)
                    print(f"{username} disconnected")
            if clients_play == 2:
                if turns % 2 == 0:
                    turn_name = clients_play_list[0]
                    target_ip = clients_play_ip[1]
                else:
                    turn_name = clients_play_list[1]
                    target_ip = clients_play_ip[0]
            else:
                turn_name = ""
            if data in ["dos", "dnf", "code"]:
                if turns % 2 == 0:
                    target_ip = clients_play_ip[1]
                else:
                    target_ip = clients_play_ip[0]
                attack_sender = turn_name
                if data == "dos":
                    current_attack = 1
                elif data == "dnf":
                    current_attack = 2
                elif data == "code":
                    current_attack = 3
                for us in clients_play_list:
                    if us != attack_sender:
                        target_user = us
                        break
                print(f"{attack_sender} send {current_attack} attack to {target_user}")
                print(f"current attack {current_attack}")
                message = f"{connections},{clients_play},{current_attack},{attack_sender},{target_user},{username},{turn_name},{target_ip}"
                send_to_all_clients(message)
                attack_sender = ""
            else:
                current_attack = 0
                attack_sender = ""
            message = f"{connections},{clients_play},{current_attack},{attack_sender},{target_user},{username},{turn_name},{target_ip}"
            send_to_all_clients(message)
        except:
            break
    print(f"[+] Connection Lost: {username}")
    if connections > 0:
        connections -= 1
    client_list.remove(connection)
    if username in client_data:
        del client_data[username]
    if username in connected_usernames:
        connected_usernames.remove(username)
    if username in clients_play_list:
        clients_play_list.remove(username)
        clients_play -= 1
    if username in clients_play_ip:
        clients_play_ip.remove(client_ip)
    message = f"{connections},{clients_play},{current_attack},{attack_sender},{target_user},{username},{turn_name},{target_ip}"
    send_to_all_clients(message)
    current_attack = 0
    attack_sender = ""
    target_user = ""
    turn_name = ""
    connection.close()


while True:
    connection, address = s.accept()
    print(f"[+] New Connection: {address}")
    connections += 1
    client_list.append(connection)
    client_ip = address[0]
    start_new_thread(threaded_client, (connection,))
