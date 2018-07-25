import durations

class Duration(object):
    """Coerce a valid duration written as a human friendly string to an
      integer value in seconds.
    """

    docs_url = 'https://github.com/oleiade/durations'

    def __init__(self, min_duration='30s', max_duration='1y'):
        self.min_duration = durations.Duration(min_duration)
        self.max_duration = durations.Duration(max_duration)
        self.min_secs = int(self.min_duration.to_seconds())
        self.max_secs = int(self.max_duration.to_seconds())

    def __call__(self, ctx, param, value):
        try:
            d = durations.Duration(value)
        except ValueError:
            msg = 'Must be a valid duration string -- see {0}'
            raise self.error(msg, self.docs_url)
        s = int(d.to_seconds())
        if s < self.min_secs:
            msg = 'Must be a minimum of {0}.'
            raise self.error(msg, self.min_duration.representation)
        if s > self.max_secs:
            msg = 'Must be a maximum of {0}.'
            raise self.error(msg, self.max_duration.representation)
        return s

    def error(self, msg, *args):
        return click.BadParameter(msg.format(*args))
