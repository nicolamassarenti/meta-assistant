import openai

from meta_assistant import logger


class TextGenerator:
    @staticmethod
    def generate(key: str, model: str, input: str, instruction: str):
        openai.api_key = key
        prompt = input + ". - " + instruction
        logger.debug("Prompt: {}".format(prompt))
        response = openai.Completion.create(
            model=model, prompt=prompt, best_of=1, max_tokens=50
        )

        return response["choices"][0]["text"]
