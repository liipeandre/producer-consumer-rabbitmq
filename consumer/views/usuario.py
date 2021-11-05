from json import loads

from consumer.models.Usuario import Usuario


def inserir(channel, method, properties, message):

    message = loads(message.decode('utf-8'))

    usuario = Usuario(
        nome=message['nome'],
        idade=message['idade']
    )

    message = {
        'status': False,
    }

    if usuario.inserir()[0]:
        message['status'] = True

    usuario.server_process_message(
        host = 'localhost',
        queue_name = 'usuario.inserir',
        message = message,
        method = method,
        correlation_id = properties.correlation_id
    )


def deletar(channel, method, properties, message):

    message = loads(message.decode('utf-8'))

    usuario = Usuario(
        id_usuario=message['id_usuario'],
    )

    message = {
        'status': False,
    }

    if usuario.deletar()[0]:
        message['status'] = True

    usuario.server_process_message(
        host = 'localhost',
        queue_name = 'usuario.deletar',
        message = message,
        method = method,
        correlation_id = properties.correlation_id
    )


def listar(channel, method, properties, message):

    usuario = Usuario()
    status, data = usuario.listar()

    message = {
        'status': status,
        'data': data,
    }

    usuario.server_process_message(
        host = 'localhost',
        queue_name = 'usuario.listar',
        message = message,
        method = method,
        correlation_id = properties.correlation_id
    )


def visualizar(channel, method, properties, message):

    message = loads(message.decode('utf-8'))

    usuario = Usuario(
        id_usuario=message['id_usuario'],
    )

    status, data = usuario.visualizar()

    message = {
        'status': status,
        'data': data,
    }

    usuario.server_process_message(
        host = 'localhost',
        queue_name = 'usuario.visualizar',
        message = message,
        method = method,
        correlation_id = properties.correlation_id
    )


def editar(channel, method, properties, message):

    message = loads(message.decode('utf-8'))

    usuario = Usuario(
        id_usuario=message['id_usuario'],
        nome=message['nome'],
        idade=message['idade']
    )

    message = {
        'status': False,
    }

    if usuario.editar()[0]:
        message['status'] = True

    usuario.server_process_message(
        host = 'localhost',
        queue_name = 'usuario.editar',
        message = message,
        method = method,
        correlation_id = properties.correlation_id
    )
