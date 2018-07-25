"""Sub command to manage legal entities.

  Run `hazy entity --help` for usage.
"""

import click

from .. import aliased

@click.group(cls=aliased.Group)
@click.pass_obj
def entity(obj):
    """Manage legal entities that can own and access data sources.

      All data in Hazy must be owned by a legal entity (the "data controller")
      and can be shared with other legal entities ("data processors").

      A legal entity is usually a company, but can also be an individual
      or another form of organisation like a partnership or a charity.

      Run `hazy entity docs` for more information.
    """

@entity.command()
@click.pass_obj
def create(obj):
    """Create a legal entity."""

    raise NotImplementedError

@entity.command()
@click.pass_obj
def show(obj):
    """Show information about a legal entity."""

    raise NotImplementedError

@entity.command()
@click.pass_obj
def update(obj):
    """Update a legal entity."""

    raise NotImplementedError

@entity.command()
@click.pass_obj
def delete(obj):
    """Delete a legal entity.

      Note that you **cannot** delete a legal entity that currently
      owns or has access to a data source.
    """

    raise NotImplementedError

@entity.command()
@click.pass_obj
def docs(obj):
    """Open the online documentation on legal entities."""

    raise NotImplementedError
