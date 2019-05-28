import sys
from subprocess import Popen, PIPE

temperature = []
sensor = Popen(['node', 'sensor.js'], stdout=PIPE)
buffer  = b''
while True:
    out = sensor.stdout.read(1)
    if out == b'\n':
        temperature.append(float(buffer))
        print(temperature)
        buffer = b''
    else:
        buffer +=out