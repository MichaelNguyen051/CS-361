import pika
import csv
import json
import random
import os


def main():
    # file_location = os.path.join(os.path.expanduser("~"), "Desktop")
    file_name = "Sightings.csv"
    # os.chdir(file_location)
    # Open the bird sightings file and read the lines
    with open(file_name, newline='') as csvfile:
        lines = list(csv.reader(csvfile))

    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='request_queue')

    # Handle incoming messages
    def on_request(ch, method, props, body):
        print("Request received")
        # Choose a random line from the CSV file
        line = random.choice(lines)

        # Convert the data to a JSON object
        data = {'line': line}
        message = json.dumps(data)

        # Send the response back to the sender
        channel.basic_publish(exchange='',
                              routing_key=props.reply_to,
                              properties=pika.BasicProperties(
                                 correlation_id=props.correlation_id
                              ),
                              body=message)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Sent line: {line}")

    # Start consuming messages
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='request_queue', on_message_callback=on_request)

    print("Waiting for requests...")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
