
class docstring(object):
    """Decorator that interpolates arguments into a function's docstring."""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, func):
        func.__doc__ = func.__doc__.format(*self.args, **self.kwargs)
        return func
