import time
import random
while True:
    time.sleep(random.random()*5)
    temperature = random.random()*20 - 5
    print(temperature, flush=True, end='')

