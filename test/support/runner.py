from click import testing
from hazy.main import cli

class CliRunner(testing.CliRunner):
    """Patch test env so that this:

          runner = CliRunner(should_lala=True)

      Is equivalent to this:

          runner = BaseCliRunner(env={'HAZY_SHOULD_LALA': 'bar', 'HAZY_TESTING': True})

    """

    def __init__(self, **kwargs):
        env = {'HAZY_TESTING': str(True)}
        for key, value in kwargs.items():
            env["HAZY_{0}".format(key.upper())] = str(value)
        super(CliRunner, self).__init__(env=env)

def invoke(*args, **kwargs):
    runner = CliRunner()
    return runner.invoke(cli, list(args), **kwargs)
