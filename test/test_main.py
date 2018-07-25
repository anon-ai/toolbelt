
from .support import runner

def test_help():
    result = runner.invoke('--help')
    assert result.exit_code == 0
    assert 'Resources' in result.output

def test_docs():
    result = runner.invoke('docs')
    assert result.exit_code == 0
    from hazy.main import DOCUMENTATION_URL as url
    assert 'Opened {0}'.format(url) in result.output
