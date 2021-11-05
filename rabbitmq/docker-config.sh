#!/bin/bash

# Criando um usuário chamado 'admin', com senha 'admin', e dando permissões de administrador.
rabbitmqctl add_user admin admin
rabbitmqctl set_user_tags admin administrator
