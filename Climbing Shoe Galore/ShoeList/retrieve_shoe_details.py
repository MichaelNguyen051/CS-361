import json
import pika
import uuid


def retrieve_shoe_list(brand, type=None, closure=None):
    shoe_list = None
    def on_message_received(ch, method, props, body):
        nonlocal shoe_list
        shoe_list = json.loads(body)[brand]
        print(f"Received response: {shoe_list}")
        connection.close()

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    reply_queue = channel.queue_declare(queue='', exclusive=True)

    channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True, on_message_callback=on_message_received)

    channel.queue_declare(queue='request-queue')

    cor_id = str(uuid.uuid4())
    print(f'Sending Request: {cor_id}')

    example_body = {'brand': brand, 'closure': closure, 'type': type}

    channel.basic_publish('', routing_key='request-queue',
                          properties=pika.BasicProperties(reply_to=reply_queue.method.queue, correlation_id=cor_id),
                          body=json.dumps(example_body))
    print("Starting Client")

    channel.start_consuming()

    return shoe_list

# a = retrieve_shoe_list("La Sportiva", "Bouldering", "Lace")
# print(a["Katana Lace Vibram XS Edge Climbing Shoe"]["Description"])