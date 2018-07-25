"""Sub command to manage sharing policies.

  Run `hazy policy --help` for usage.
"""

import click

from .. import aliased

@click.group(cls=aliased.Group)
@click.pass_obj
def policy(obj):
    """Manage data sharing policies and legal terms.

      Hazy allows data to be shared by its owner (the "data controller") with
      other entities ("data processors"). In order to enable this, the data owner
      must create a data sharing policy.

      A policy defines the legal basis for the data sharing (the purpose and
      scope of the data processing) and can enforce access restrictions.

      Run `hazy policy docs` for more information.
    """

@policy.command()
@click.pass_obj
def create(obj):
    """Create a data sharing policy."""

@policy.command()
@click.pass_obj
def show(obj):
    """Show information about a data sharing policy."""

    raise NotImplementedError

@policy.command()
@click.pass_obj
def update(obj):
    """Update a data sharing policy."""

    raise NotImplementedError

@policy.command()
@click.pass_obj
def archive(obj):
    """Archive a data sharing policy."""

    raise NotImplementedError

@policy.command()
@click.pass_obj
def delete(obj):
    """Delete a data sharing policy."""

    raise NotImplementedError

@policy.command()
@click.pass_obj
def docs(obj):
    """Open the online documentation on data sharing policies."""

    raise NotImplementedError
