import inspect


def extension(cls: type):
    def wrap(cls):
        target = cls.__bases__[0]
        for name, attr in inspect.getmembers(cls):
            if not name.startswith('__') and not hasattr(target, name):
                setattr(target, name, attr)
        return cls

    if cls is None:
        return wrap

    return wrap(cls)
