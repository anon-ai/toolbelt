"""Sub command to manage data sources.

  Run `hazy source --help` for usage.
"""

import click

from .. import aliased

@click.group(cls=aliased.Group)
@click.pass_obj
def source(obj):
    """Connect and manage data sources.

      All data in Hazy originates from a source. This can be an online database,
      a cloud storage bucket or a manually ingested file.

      Run `hazy source docs` for more information.
    """

@source.command()
@click.pass_obj
def create(obj):
    """Create a data source."""

@source.command()
@click.pass_obj
def show(obj):
    """Show information about a data source."""

    raise NotImplementedError

@source.command()
@click.pass_obj
def update(obj):
    """Update a data source."""

    raise NotImplementedError

@source.command()
@click.pass_obj
def archive(obj):
    """Archive a data source."""

    raise NotImplementedError

@source.command()
@click.pass_obj
def delete(obj):
    """Delete a data source."""

    raise NotImplementedError

@source.command()
@click.pass_obj
def docs(obj):
    """Open the online documentation on data sources."""

    raise NotImplementedError
