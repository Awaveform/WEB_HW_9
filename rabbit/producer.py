import pika
import json

from config_interactions import get_config_value
from rabbit.rabbit_connect import make_exchange_queue_bind


def publish_author_info(author_name: str = None, author_part_link: str = None):
    channel, connection = make_exchange_queue_bind()
    message = {
        "name": author_name,
        "link": author_part_link
    }
    channel.basic_publish(
        exchange=get_config_value("RABBIT_MQ", "exchange_name"),
        routing_key=get_config_value("RABBIT_MQ", "queue_name"),
        body=json.dumps(message).encode(),
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        ),
    )
    print(" [x] Sent %r" % message)
    connection.close()


