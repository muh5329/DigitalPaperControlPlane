import typer
import fileio

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


@app.command()
def upload(dir: str):
    """
    draw
    """
    print(f"Uploading all files in  : {dir}")
    fileio.upload_files_to_dpt(dir)
    typer.echo("upload")


