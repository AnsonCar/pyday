import typer
from opencc import OpenCC

app = typer.Typer(no_args_is_help=True)

@app.command()
def version():
    typer.echo("0.1.0")

@app.command()
def changeLang(lang:str=''):
    typer.echo("Shooting portal gun")