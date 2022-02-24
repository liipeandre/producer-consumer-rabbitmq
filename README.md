# Producer-Consumer with Flask, RabbitMQ, Docker and Docker Compose

## Author

- André Felipe Pereira dos Santos

## Description

This project is a simple web application using Python and Flask, in a publish-subscribe architecture and using RabbitMQ
as message broker. In this project:

- A producer (producer), developed in Flask, creates messages in JSON format for the consumer in a request queue;

- A consumer (consumer) reads the messages, converts them and performs operations on a SQLite database, returning
their result to the producer (producer), through another queue of responses;
 
- RabbitMQ keeps the messages and makes the connection between the producer (producer) and the consumer (consumer)

RabbitMQ must be configured in a Docker container, using the files from the 'rabbitmq' folder.

