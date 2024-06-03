import typer
import fileio

app = typer.Typer()


@app.callback()
def callback():
    """
    appy
    """


@app.command()
def render(draw_action: str):
    """
    draw
    """
    print(f"Rendering : {draw_action}")

    if draw_action == "random":
        fileio.pick_a_random_file_flip_to_page()


@app.command()
def upload(dir: str):
    """
    draw
    """
    print(f"Uploading all files in  : {dir}")
    fileio.upload_files_to_dpt(dir)
    typer.echo("upload")


