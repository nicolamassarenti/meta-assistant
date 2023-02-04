# meta-assistant

An MVP of a virtual assistant that chats with you.

## In a nutshell

![meta-assistant](https://raw.githubusercontent.com/nicolamassarenti/meta-assistant/main/docs/head.gif)

This application allows a user to talk and chat with a virtual assistant hosted in Nvidia Audio2Face tool.
The key features are:
* **Audio recorded** from the micropghone in chunks and stopped when the user presses button 'q'
* Audio is sent to Google Cloud for **Speech-To-Text** conversion
* Text is sent to **OpenAI** for **text generation**
* Generated text is sent to Google Cloud for **Text-to-Speech** conversion
* Audio is sent via gRPC to **Nvidia Audio2Face** streaming server


## Setup
### Local development
To install the application locally, you need to have [poetry](python-poetry.org) installed. To install the dependencies, run the following command:
```bash
poetry install
```

Before running the application, remember to open [Nvidia Omniverse Audio2Face](https://developer.nvidia.com/omniverse-audio2face) 
and to activate the streaming gRPC server. You can do it by clicking on `Audio2Face`, then click on `Open Demo Scene` and then on 
`Full Face Core + Streaming Player`. See image below for reference.

![](https://raw.githubusercontent.com/nicolamassarenti/meta-assistant/main/docs/a2f-streaming-setup.png)

In addition, you have to have a Google Cloud account and a Google Cloud project with the following APIs enabled:
- Google Speech-to-Text API
- Google Text-to-Speech API

Then, you have to create a service account and download the JSON key file. 

You also have to have a valid OpenAI API key.

Finally, you have to set the following environment variables:
```bash
GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
OPENAI_KEY="your-openai-key"
OPENAI_MODEL="text-davinci-003" # or any other model you want to use
```

Then, you're ready to run the application:
```bash
GRPC_SERVER="localhost:50051"
OPENAI_INSTRUCTION="answer to this sentence like you are chatting with a friend"

poetry run python -m meta_assistant \
    --grpc-server=$GRPC_SERVER \
    --openai-instruction=$OPENAI_INSTRUCTION
```


### Contributing
If you want to contribute to this project, please read the [contributing guidelines](CONTRIBUTING.md).

### License
This project is licensed under the terms of the MIT license.

### Authors
* [Nicola Massarenti](nicolamassarenti.com)
