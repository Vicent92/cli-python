#!/usr/bin/env python
import json
import click

@click.group()
def cli():
    pass

@cli.command()
def hola():
    """Imprime un saludo"""
    with open('data_task.json', "r", encoding="utf-8") as f:
        datos = json.load(f)
        for task in datos:
            click.echo(f"{task['id']}: {task['name']}")

    click.echo("¡Hola, mundo!")

if __name__ == "__main__":
    cli()



