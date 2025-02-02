#!/usr/bin/env python
import json
import click

FILE_DATA = "data_task.json"

def read_data():
    with open(FILE_DATA, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos

def write_data(datos):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)

@click.group()
def cli():
    pass

@cli.command()
def tasks():
    datos = read_data()

    if len(datos) == 0:
        click.echo("No hay tareas")
        return
        
    for task in datos:
        click.echo(f"{task['id']}: {task['description']}")

@cli.command()
@click.option("--description", help="De que se trata la nueva tarea", required=True)
def add(description):
    datos = read_data()
    newTask = {
        "id": len(datos) + 1,
        "description": description,
        "status": "pendiente",
        "createdAt": "2021-05-06",
        "updatedAt": "2021-05-06"
    }

    datos.append(newTask)
    write_data(datos)

    click.echo("Tarea agregada")

@cli.command()
@click.option("--id", help="ID de la tarea a eliminar", required=True, type=int)
def delete(id):
    datos = read_data()
    findTask = next((d for d in datos if d["id"] == id), None)

    datos.remove(findTask)
    write_data(datos)

    click.echo(f"Tarea con el id {id} eliminada")

@cli.command()
@click.option("--id", help="ID de la tarea a eliminar", required=True, type=int)
@click.option("--description", help="De que se trata la nueva tarea", required=False)
@click.option("--status", help="En que estado esta la tarea", required=False)
def update(id, description, status):
    datos = read_data()

    for task in datos:
        if task["id"] == id:
            if description:
                task["description"] = description
            if status:
                task["status"] = status

    write_data(datos)

    



if __name__ == "__main__":
    cli()



