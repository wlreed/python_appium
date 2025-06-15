class Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instance = None
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]
