from consumer.database.Database import Database
from rabbitmq.RabbitMQ import RabbitMQ


class Usuario(RabbitMQ):
    id_usuario = None
    nome = None
    idade = None

    def inserir(self):
        database = Database()
        query = """
            insert into usuario (nome, idade)
            values (:nome, :idade);
        """
        status, data = database.execute_sql_query(query, self.__dict__)
        database.commit()
        return status, data


    def deletar(self):
        database = Database()
        query = """
            delete from usuario
            where id_usuario = :id_usuario;
        """
        status, data = database.execute_sql_query(query, self.__dict__)
        database.commit()
        return status, data


    def listar(self):
        database = Database()
        query = """
            select id_usuario, nome, idade from usuario;
        """
        status, data = database.execute_sql_query(query, self.__dict__)
        database.commit()
        return status, data


    def visualizar(self):
        database = Database()
        query = """
            select id_usuario, nome, idade from usuario
            where id_usuario = :id_usuario;
        """
        status, data = database.execute_sql_query(query, self.__dict__)
        database.commit()
        return status, data


    def editar(self):
        database = Database()
        query = """
            update usuario set 
            nome = :nome, 
            idade = :idade
            where id_usuario = :id_usuario;
        """
        status, data = database.execute_sql_query(query, self.__dict__)
        database.commit()
        return status, data