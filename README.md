# alexa-chatbot

A simple (just-for-fun)-project for the Alexa Voice Service using [alexa-client](https://github.com/ewenchou/alexa-client) and [simple-tts](https://github.com/ewenchou/simple-tts) by ewenchou and the [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition) library.

The main.py script uses the alexa-client to create a simple alexa-chatbot (fully text in- and output). It uses the simple-tts to create the input audio for the AVS and the SpeechRecognition-Library to transcribe the answer. Therefore, the time of the response is quite high and its quality depends on the speech recognition.

**NOTE**: This script is a modification of the main.py script in the [ewenchou/alexa-tts-demo](https://github.com/ewenchou/alexa-tts-demo) Github repository. All thanks goues to [ewenchou](https://github.com/ewenchou) for his nice tools

# Prerequisites

This script was designed and tested on Ubuntu 14.04

# Installation

Requires the following libraries:

* [alexa-client](https://github.com/ewenchou/alexa-client)

* [simple-tts](https://github.com/ewenchou/simple-tts)

* [SpeechRecognition](https://pypi.python.org/pypi/SpeechRecognition)

# Run

To run just start the main.py script

```
python main.py
```