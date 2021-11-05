from os import getcwd
from sqlalchemy import create_engine


class Database:
    def __init__(self):
        self.database = None
        self.transaction = None

        self.create_connection()
        self.begin_transaction()


    def create_connection(self):
        file_dir = getcwd()

        # TODO: Editar a URI de acesso ao banco de dados, caso necessário.
        uri = "{database_type}:///{database_name}".format(
            database_type='sqlite',
            database_name=file_dir + '/database/database.db'
        )

        engine = create_engine(uri)
        self.database = engine.connect()


    def begin_transaction(self):
        self.transaction = self.database.begin()


    def execute_sql_query(self, query: str, parameters: dict):
        try:
            output = self.database.execute(query, parameters)
            output = output.fetchall() if output.returns_rows else []

            data = [dict(registry) for registry in output]

            return True, data

        except Exception as exception:
            self.rollback()
            return False, []


    def commit(self):
        try:
            self.transaction.commit()
            return True

        except Exception as exception:
            self.rollback()
            return False


    def rollback(self):
        self.transaction.rollback()
