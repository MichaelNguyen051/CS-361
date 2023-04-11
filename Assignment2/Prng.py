from time import sleep
import random

prng_service = "prng_service.txt"
while True:
    sleep(3)
    read_service = open(prng_service, "r")
    line = read_service.read()
    print(f"{line} is read")
    read_service.close()
    if line == "run":
        print("statement occurred")
        num_gen = random.randint(0, 1000)
        write_service = open(prng_service, "w")
        write_service.write(str(num_gen))
        write_service.close()
        print("prng file completed")
    else:
        print("line not read")
    sleep(1)
