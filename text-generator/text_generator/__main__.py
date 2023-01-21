import typer

from text_generator import logger
from text_generator.services import Generator

app = typer.Typer()


@app.command()
def generate(
    key: str = typer.Option(..., help="OpenAI API key", envvar="OPEN_AI_API_KEY", show_envvar=True),
    model: str = typer.Option(..., help="OpenAI model", envvar="OPEN_AI_MODEL", show_envvar=True),
    input: str = typer.Option(..., help="Input text"),
    instruction: str = typer.Option(..., help="Instruction text"),
):
    logger.debug("Received parameters: key={}, model={}, input={}, instruction={}".format(key, model, input, instruction))
    logger.info("Generating text...")
    result = Generator.generate(key=key, model=model, input=input, instruction=instruction)

    logger.info("Result: {}".format(result))

if __name__ == "__main__":
    app()
