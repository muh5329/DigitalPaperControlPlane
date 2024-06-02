import typer
from dptrp1 import LookUpDPT

app = typer.Typer()


@app.callback()
def callback():
    """
    appy
    """


@app.command()
def draw():
    """
    draw
    """
    typer.echo("draw")


