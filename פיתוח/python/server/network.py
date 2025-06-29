import socket
from _thread import *


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.56.1"
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = 9090
        self.address = (self.server, self.port)
        self.connections = 0
        self.clients_play = 0
        self.connect()
        self.current_attack = 0
        self.attack_sender = ""
        self.target_user = ""
        self.turn_name = ""
        self.clients_connected = []
        self.target_ip = self.ip

    def connect(self):
        try:
            self.client.connect(self.address)
            start_new_thread(self.receive_data, ())
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)

    def receive_data(self):
        while True:
            try:
                data = self.client.recv(2048).decode().split(",")
                if len(data) >= 8:
                    connections = int(data[0])
                    clients_play = int(data[1])
                    self.connections = connections
                    self.clients_play = clients_play
                    self.current_attack = int(data[2])
                    self.attack_sender = data[3]
                    self.target_user = data[4]
                    self.clients_connected = data[8:]
                    self.turn_name = data[6]
            except:
                pass

    def get_connections(self):
        return self.connections

    def get_clients_play(self):
        return self.clients_play

    def get_current_attack(self):
        return self.current_attack

    def get_attack_sender(self):
        return self.attack_sender

    def get_clients_connected(self):
        return self.clients_connected

    def get_target_user(self):
        return self.target_user

    def get_turn_name(self):
        return self.turn_name

    def get_target_ip(self):
        return self.target_ip

    def is_username_connected(self, username):
        return username in self.clients_connected
