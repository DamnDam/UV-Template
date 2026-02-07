import typer

app = typer.Typer()


@app.command()
def main():
    """Main entry point for the CLI."""
    typer.echo("Hello, World!")
