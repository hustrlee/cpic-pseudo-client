import pika

MQ_DEFAULT_HOST = "localhost"
MQ_DEFAULT_EXCHANGE = "case_exchange"
MQ_DEFAULT_QUEUE = "case_queue"


class CasePublisher(object):

    def __init__(self, ) -> None:
        return

    def connect(self, host=MQ_DEFAULT_HOST, exchange=MQ_DEFAULT_EXCHANGE, queue=MQ_DEFAULT_QUEUE):
        self._host = host
        self._exchange = exchange
        self._queue = queue

        param = pika.ConnectionParameters(self._host)
        self._connection = pika.BlockingConnection(param)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(exchange=self._exchange, exchange_type="fanout", durable=True)  # noqa
        self._channel.queue_declare(queue=self._queue, durable=True)
        self._channel.queue_bind(queue=self._queue, exchange=self._exchange, routing_key="")  # noqa

    def close(self):
        self._channel.close()
        self._connection.close()

    def publish(self, msg):
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key="",
            body=msg,
            properties=pika.BasicProperties(delivery_mode=2)
        )


mq = CasePublisher()
