import typer


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


