
import click
import webbrowser

from . import flags

def open(url):
    result = do_open(url)
    if result:
        msg = 'Opened {0}'.format(url)
        click.secho(msg, fg='green')
    else:
        msg = 'Failed to open {0}'.format(url)
        click.secho(msg, fg='red')
    return result

def do_open(url):
    if flags.is_testing() and not flags.should_open_browser():
        return True
    return webbrowser.open_new_tab(url)
