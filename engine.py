
import sqlalchemy.engine


class Engine:
    """
    This class is a singleton, meaning that the first time it's called, it will create an engine
    and return that same engine every time the class is called.  Thus, a single engine is created
    every time the app is run, instead of every time a session is instantiated.
    """

    _engine = None
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
            cls._engine = Engine._get_engine(**kwargs)
        return cls._engine

    @staticmethod
    def _get_engine(**kwargs):
        """
        This function creates and returns a SQLAlchemy engine
        :param kwargs: This name of the database is pulled from kwargs
        :return: a SQLALchemy engine
        """
        engine_name = 'MySQL'
        return engine_name


def main():
    x = Engine()
    print(x)
    y = Engine()
    print(y)

if __name__ == '__main__':
    main()