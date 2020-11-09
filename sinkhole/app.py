import os
import json
import click
import requests


NOMAD_ADDR = os.getenv('NOMAD_ADDR', 'http://localhost:4646')


@click.group()
def cli():
    """Command line tool to add webhook sinks for Nomad events."""
    click.echo('Try using with the create, list or remove subcommands.')
    click.echo(f'Nomad server currently set to: {NOMAD_ADDR}')


# Subcommands
@click.command()
@click.option('--id', required=True, default='default', help='ID of webhook')
# @click.option('--topics', default='*', help='Topics to sink')
# @click.option('--events', default='*', help='Events to sink')
@click.argument('url', required=True)
def create(id, url):
    """Create a new Nomad event sink webhook."""
    click.echo(f'Creating new sink {id} at address {url}...')
    data = {
        "ID": id,
        "Address": url,
        "Type": "webhook",
        "Topics": {
            "*": ["*"]
        }
    }
    response = requests.post(
        f'{NOMAD_ADDR}/v1/event/sink/{id}',
        data=json.dumps(data))
    if response.status_code == 200:
        click.echo(f'Webhook created and sending events to {url}!')
        return True
    else:
        print(response.text)
        click.echo(f'Something went wrong... Code {response.status_code}!')


cli.add_command(create)
