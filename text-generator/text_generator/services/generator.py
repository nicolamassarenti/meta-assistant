import openai

from text_generator import logger


class Generator:
    @staticmethod
    def generate(key: str, model: str, input: str, instruction: str):
        openai.api_key = key
        prompt = input + ". - " + instruction
        logger.debug("Prompt: {}".format(prompt))
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            best_of=5
        )

        return response["choices"][0]["text"]

