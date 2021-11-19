import pika


class CaseQueue(object):

    def __init__(self, host="localhost", exchange="medical_review") -> None:
        self._host = host
        self._exchange = exchange

    def create(self):
        param = pika.ConnectionParameters(self._host)
        self._connection = pika.BlockingConnection(param)
        self._channel = self._connection.channel()
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type="fanout",
            durable=True
        )

    def close(self):
        self._channel.close()
        self._connection.close()

    def publish(self, msg):
        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key="",
            body=msg,
            properties=pika.BasicProperties(
                delivery_mode=2
            )
        )


MQ_HOST = "localhost"
MQ_EXCHANGE = "medical_review"

mq = CaseQueue(host=MQ_HOST, exchange=MQ_EXCHANGE)
