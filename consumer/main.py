import views.usuario
from rabbitmq.RabbitMQClient import RabbitMQClient


def main():
    queues = [
        'usuario.inserir',
        'usuario.deletar',
        'usuario.listar',
        'usuario.visualizar',
        'usuario.editar',
    ]

    message_broker = RabbitMQClient('localhost')

    if message_broker.is_connected():
        for queue_name in queues:

            request_queue_name, response_queue_name = message_broker.get_queue_names(queue_name)

            on_message_callback = queue_name.split('.')[1]
            on_message_callback = getattr(views.usuario, on_message_callback)

            message_broker.create_queue(request_queue_name)
            message_broker.create_queue(response_queue_name)

            message_broker.async_receive_message(request_queue_name, on_message_callback)

        message_broker.async_start_consuming()


if __name__ == '__main__':
    main()
