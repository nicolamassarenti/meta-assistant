# meta-assistant

An MVP of a virtual assistant that chats with you.

## In a nutshell

![meta-assistant]()

This application allows a user to talk and chat with a virtual assistant hosted in Nvidia Audio2Face tool.
The key features are:
* Audio recorded in chunks and stopped when the user presses button 'q'
* Audio is sent to Google Cloud for speech to text conversion
* Text is sent to OpenAI for text generation
* Generated text is sent to Google Cloud for Text to Speech conversion
* Audio is sent via gRPC to Nvidia Audio2Face streaming server


## Setup
### Local development
To install the application locally, you need to have poetry installed. Then run the following commands:
```bash
poetry install
```

To run the application, first you need to run [Nvidia Omniverse Audio2Face](https://developer.nvidia.com/omniverse-audio2face) and then run the following command:
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