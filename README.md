# meta-assistant

An MVP of a virtual assistant that chats with you.

## In a nutshell

![meta-assistant](https://raw.githubusercontent.com/nicolamassarenti/google-stt-openai-gpt-nvidia-audio2face/main/docs/head.gif?token=GHSAT0AAAAAAB5QRTREWHXNCEY56A273FP2Y664UGA)

This application allows a user to talk and chat with a virtual assistant hosted in Nvidia Audio2Face tool.
The key features are:
* **Audio recorded** from the micropghone in chunks and stopped when the user presses button 'q'
* Audio is sent to Google Cloud for **Speech-To-Text** conversion
* Text is sent to **OpenAI** for **text generation**
* Generated text is sent to Google Cloud for **Text-to-Speech** conversion
* Audio is sent via gRPC to **Nvidia Audio2Face** streaming server


## Setup
### Local development
To install the application locally, you need to have poetry installed. Then run the following commands:
```bash
poetry install
```

Before running the application, remember to open [Nvidia Omniverse Audio2Face](https://developer.nvidia.com/omniverse-audio2face) 
and to activate the streaming gRPC server. You can do it by clicking on `Audio2Face`, then click on `Open Demo Scene` and then on 
`Full Face Core + Streaming Player`. See image below for reference.

[]()
```bash
```

### Docker
TODO


### Next steps
* Stream audio from the microphone
* Send audio to Google STT via streaming
* Send text to OpenAI via streaming
* Send text to Google TTS via streaming
* Test alternative for TTS with focus on speech audio quality



### Contributing
If you want to contribute to this project, please read the [contributing guidelines](CONTRIBUTING.md).

### License
This project is licensed under the terms of the [MIT license](LICENSE).

### Authors
* [Nicola Massarenti](nicolamassarenti.com)