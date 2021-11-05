# Usando a imagem base 'rabbitmq', disponível no Docker Hub
FROM rabbitmq

# Copiando o script 'rabbitmq-init.sh' para a pasta init.d do contâiner Docker
ADD config_files/enabled_plugins /etc/rabbitmq/enabled_plugins
ADD docker-config.sh /home

# Dando permissões de execução para o script
RUN chmod +x /home/docker-config.sh
RUN chown root:root /home/docker-config.sh
