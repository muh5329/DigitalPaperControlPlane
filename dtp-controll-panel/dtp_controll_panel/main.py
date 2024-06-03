import typer
import fileio
from dptrp1.dptrp1 import DigitalPaper

app = typer.Typer()


@app.callback()
def callback():
    """
    appy
    """


@app.command()
def render(art: str):
    """
    draw
    """
    print(f"Rendering : {art}")

    
    
    

    if art == "random":
        typer.echo("rendering random art")

    typer.echo("draw")


