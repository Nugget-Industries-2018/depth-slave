#!/usr/bin/env python
import socket
from ms5837 import ms5837

TCP_IP = 'localhost'
TCP_PORT = 8083
BUFFER_SIZE = 1024

sensor = ms5837.MS5837_30BA()
if not sensor.init():
    print('bar30 sensor could not be initialized')
    exit(1)

Pair = 1013.25  # Pascals
rho  = 998.23   # kg/m3
g    = 9.8      # m/s2

offset = 0


def calc_depth(pressure):
    return (pressure - Pair) * 100 / (rho * g)


def process_cmd(cmd):
    global offset
    sensor.read()

    if cmd == 'P':
        return sensor.pressure()
    elif cmd == 'p':
        return sensor.pressure() - offset
    elif cmd == 'D':
        return calc_depth(process_cmd('P'))
    elif cmd == 'd':
        return calc_depth(process_cmd('p'))
    elif cmd == 'Z':
        offset = sensor.pressure()
    else:
        return 'command not recognized: {}'.format(cmd)

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    print('PYTHON: listening at {}:{}'.format(TCP_IP, TCP_PORT))

    conn, addr = s.accept()
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        data = str(data).rstrip('\n')
        print('PYTHON: received: ', data)
        conn.send(str(process_cmd(data)))
