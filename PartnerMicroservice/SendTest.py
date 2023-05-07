import pika
import json
import uuid


def main():
    # Connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for the response
    result = channel.queue_declare(queue='', exclusive=True)
    callback_queue = result.method.queue

    # Define the function to handle the response
    def on_response(ch, method, props, body):
        if props.correlation_id == corr_id:
            data = json.loads(body)
            print(f"Received response: {data}")
            channel.stop_consuming()

    # Generate a correlation ID for the request
    corr_id = str(uuid.uuid4())

    # Define the request message
    message = "Hello, server!"

    # Send the request message and wait for the response
    channel.basic_publish(exchange='',
                          routing_key='request_queue',
                          properties=pika.BasicProperties(
                                reply_to=callback_queue,
                                correlation_id=corr_id,
                          ),
                          body=message)

    # Start consuming responses
    channel.basic_consume(queue=callback_queue, on_message_callback=on_response)

    print(f"Sending request: {message}")
    channel.start_consuming()


if __name__ == '__main__':
    main()
