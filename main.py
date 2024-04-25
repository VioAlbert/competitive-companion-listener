import json
import os
import shutil
import socket
import sys

HOST = ''
PORT = 10043

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

print('Waiting for connections...')
s.listen(1)
conn, addr = s.accept()

print('Connected with ' + addr[0] + ':' + str(addr[1]))

resp = conn.recv(4096)
if not resp: sys.exit(0)
msg = resp.decode()
body = msg[msg.find('\r\n\r\n')+4:]
conn.close()

data = json.loads(body)

OUTPUT_DIR = 'sample'

if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
else:
    for filename in os.listdir(OUTPUT_DIR):
        file_path = os.path.join(OUTPUT_DIR, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

num_tc = 1
for test in data['tests']:
    file_path = os.path.join(OUTPUT_DIR, str(num_tc))
    f_input = open(file_path + '.in', 'a')
    f_input.write(test['input'])
    f_input.close();
    f_output = open(file_path + '.ans', 'a')
    f_output.write(test['output'])
    f_output.close();
    num_tc += 1

print('Downloaded testcases.')
