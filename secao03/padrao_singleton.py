

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.intance = super(Singleton, cls).__new__(cls)
            print(f"Criando o objeto {cls.intance}")
        return cls.instance

s1 = Singleton()
print(f'Intancia: 1: {id(s1)}')

s2 = Singleton()
print(f'Intancia 2: {id(s2)}')

