from rabbitmq.RabbitMQ import RabbitMQ


class Usuario(RabbitMQ):
    id_usuario = None
    nome = None
    idade = None

    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)
        super().__init__(iterable, **kwargs)