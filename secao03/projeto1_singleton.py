import sqlite3


class Singleton(type):

    __instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)


class Database(metaclass=Singleton):

    connection = None

    def connect(self):
        if self.connection is None:
            print(f'Não temos ainda uma conexão...vamos cria-la...')
            self.connection = sqlite3.coonect('db.geek')
            self.cursor = self.connection.cursor()
        return self.cursor


db1 = Database().connect()
db2 = Database().connect()

