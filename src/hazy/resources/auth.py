"""Sub command to manage authentication.

  Run `hazy source --help` for usage.
"""

import click
import requests

from .. import aliased
from ..util import interpolate
from ..validators import duration
from tinynetrc import Netrc


@click.group(cls=aliased.Group)
@click.pass_obj
def auth(obj):
    """Login and manage local toolbelt authentication."""


@auth.command()
@click.option('--email', prompt='Email', metavar='ADDRESS', help='Your email address.')
@click.option('--expires-in', metavar='DURATION', default='2 weeks',
                              callback=duration.Duration(),
                              help='How long do you want to stay logged in for?',
                              show_default=True)
@click.option('--token', metavar='ACCESS_TOKEN', help='Your API access token.')
@click.pass_obj
@interpolate.docstring(duration.Duration.docs_url)
def login(obj, email, expires_in, token):
    """Login with your Hazy credentials.

          hazy login

      This will prompt for your email and password. Alternatively, you can
      provide `--email` and `--token` directly:

          hazy login --email YOUR_EMAIL --token YOUR_ACCESS_TOKEN

      This is useful for automated scripts.

      Durations are written in human friendly string format as documented here:
      {0}
    """

    if token:
        return login_with_token(email, expires_in, token)

    password = click.prompt('Password', hide_input=True)
    return login_with_password(email, expires_in, password)


def login_with_password(email, expires_in, password):
    """Authenticate against the web service with the email and password.

      If successful, store the resulting access token in `~/.netrc`.
    """

    payload = { 'user[email]': email, 'user[password]': password }
    r = requests.post('http://localhost:4002/api/v2/auth', data=payload)
    if r.status_code == 200:
        data = r.json()['data']
        netrc = Netrc()
        netrc['localhost'] = {
            'login': data['email'],
            'password': data['token']
        }
        netrc.save()
    else:
        print("Authentication error")

def login_with_token(email, expires_in, token):
    """Authenticate against the web service with the email and access token.

      If successful, store the resulting access token in `~/.netrc`.
    """

    # msg = 'Forbidden. Have you logged in with the right credentials?'
    # click.secho(msg, fg='red')
    # raise click.Abort()
    raise NotImplementedError


@auth.command()
@click.pass_obj
def logout(obj):
    """Logout and clear local toolbelt credentials."""

    netrc = Netrc()
    netrc.pop('localhost', None)
    netrc.save()

@auth.command()
@click.pass_obj
def token(obj):
    """Display the current access token."""

    netrc = Netrc()
    print(netrc['localhost']['password'])

@auth.command()
@click.pass_obj
def whoami(obj):
    """Display the current logged in user."""

    netrc = Netrc()
    print(netrc['localhost']['login'])

@auth.command()
@click.pass_obj
def docs(obj):
    """Open the online documentation on authentication."""

    raise NotImplementedError
