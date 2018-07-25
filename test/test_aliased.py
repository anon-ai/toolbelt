
from hazy.main import DOCUMENTATION_URL as url

from .support import runner

def test_():
    result = runner.invoke()
    assert result.exit_code == 0
    assert 'Opened' not in result.output

def test_d():
    result = runner.invoke('d')
    assert result.exit_code == 0
    assert 'Opened {0}'.format(url) in result.output

def test_do():
    result = runner.invoke('do')
    assert result.exit_code == 0
    assert 'Opened {0}'.format(url) in result.output

def test_doc():
    result = runner.invoke('doc')
    assert result.exit_code == 0
    assert 'Opened {0}'.format(url) in result.output

def test_docs():
    result = runner.invoke('docs')
    assert result.exit_code == 0
    assert 'Opened {0}'.format(url) in result.output

def test_docss():
    result = runner.invoke('docss')
    assert result.exit_code == 2
    assert 'No such command' in result.output
