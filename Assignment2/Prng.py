from time import sleep
import random

while True:
    sleep(1)
    read_service = open("prng-service.txt", "r")
    line = read_service.read()
    read_service.close()
    if line == "run":
        num_gen = random.randint(0, 1000)
    write_service = open("prng-service.txt", "w")
    write_service.write(str(num_gen))
    write_service.close()
    print("prng file completed")
    sleep(3)
