import random
from time import sleep

prng_service = "prng_service.txt"
image_service = "image_service.txt"
while True:
    response = input("Please type 1 to generate an image\nor 2 to exit:\n")
    if response == "1":
        write_service = open(prng_service, "w")
        write_service.write("run")
        write_service.close()
        sleep(5)
        read_service = open(prng_service, "r")
        num_input = read_service.read()
        # read_service.close()
        new_number = random.randint(1, 1000)
        write_image = open(image_service, "w")
        write_image.write(str(new_number))
        # write_image.close()
        sleep(5)
        read_image = open(image_service, "r")
        path = read_image.read()
        print(path)
        read_image.close()
        read_service.close()
    elif input == "2":
        break
    else:
        print("unknown option")

