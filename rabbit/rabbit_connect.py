from typing import Tuple

import pika
from pika.adapters.blocking_connection import BlockingChannel, BlockingConnection
from config_interactions import get_config_value


def make_channel() -> Tuple[BlockingChannel, BlockingConnection]:
    credentials = pika.PlainCredentials(
        get_config_value("RABBIT_MQ", "user"),
        get_config_value("RABBIT_MQ", "pass"),
    )
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=get_config_value("RABBIT_MQ", "host"),
            port=get_config_value("RABBIT_MQ", "port"),
            credentials=credentials
        )
    )
    channel = connection.channel()
    return channel, connection


def make_exchange_queue_bind(exchange_name=get_config_value(
            "RABBIT_MQ",
            "exchange_name"
        ),
        queue_name=get_config_value(
            "RABBIT_MQ",
            "queue_name"
        )):
    channel, connection = make_channel()

    channel.exchange_declare(exchange=exchange_name, exchange_type="direct")
    channel.queue_declare(queue=queue_name, durable=True)
    channel.queue_bind(exchange=exchange_name, queue=queue_name)
    return channel, connection
