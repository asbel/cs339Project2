import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('hello'.encode(), ('67.163.37.156', 7999))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto('hello'.encode(), ('localhost', 8000))
