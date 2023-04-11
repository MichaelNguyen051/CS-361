import random
from time import sleep
import cv2

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
        new_number = read_service.read()
        read_service.close()
        write_image = open(image_service, "w")
        write_image.write(str(new_number))
        write_image.close()
        sleep(3)
        read_image = open(image_service, "r")
        path = read_image.read()
        image = cv2.imread(path)
        cv2.imshow("image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        read_image.close()
    elif input == "2":
        break
    else:
        print("unknown option")

