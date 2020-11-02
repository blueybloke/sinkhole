import click
import os
import requests


@click.command()
def cli():
    """A command line tool to add webhook sinks for Nomad events."""
    click.echo('Hello world!')
