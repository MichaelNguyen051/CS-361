from time import sleep

image_service = "image_service.txt"
while True:
    sleep(1)
    read_service = open(image_service, "r")
    line = read_service.read()
    read_service.close()
    try:
        number = int(line)
        photo_selector = number % 3 + 1
        path = "/Users/micha/PycharmProjects/CS-361/Assignment2/cs361/" \
               + str(photo_selector) + ".jpg"
        write_service = open(image_service, "w")
        write_service.write(path)
        write_service.close()
    except ValueError:
        print("Number not present")
