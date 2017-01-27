"""Simple "chatbot" script for the AlexaClient. This builds on the alexa-tts-demo of @ewenchoi.
"""
from alexa_client import AlexaClient
import simple_tts
import subprocess
import shlex
import os
import speech_recognition as sr
from pydub import AudioSegment

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def play_mp3(filename, padding=True, pad_each=False):
    """Plays MP3 audio file(s).

    Uses the shell command `mpg123` to play the MP3 file(s).

    Args:
        filename (str or list): File(s) to play.
        padding (bool): Whether to add a 1 second silent padding before the
                        first mp3 file to improve audio.
        pad_each (bool): Whether to add a 1 second silent padding before
                         each file in the list.

    Returns:
        None
    """
    cmd = "mpg123 "
    cmd_args = ["-q", ]
    pause = "{}/1sec.mp3".format(BASE_PATH)
    if padding:
        cmd_args.append(pause)
    if isinstance(filename, list):
        if pad_each:
            for f in filename:
                cmd_args.append(pause)
                cmd_args.append(f)
        else:
            cmd_args += filename
    else:
        cmd_args.append(filename)
    cmd += " ".join(cmd_args)
    cmd = shlex.split(cmd)
    # Use subprocess.Popen() and communicate() so the audio isn't cut off
    p = subprocess.Popen(cmd)
    p.communicate()


def text_to_audio(text):
    """This function uses the simple_tts
      @ewenchou and his alexa client to
      send a request to the AVS, saves the answer
      and gives back the corresponding path

    Args:
        text (string): The request for avs

    Returns:
        the path to the audio with the answer
        of the AVS
    """
    global alexa
    # Perform tts
    audio_command = simple_tts.tts(text)
    # Send the command to Alexa
    audio_response = alexa.ask(audio_command)
    return audio_response


def audio_to_text(audio_path):
    """A simple function, that takes a
    .mp3 audio file, converts it to .wav
    and the use a speech recognition api
    to transcribe to text.

    Args:
        audio_path (string): path to the mp3

    Returns:
        the transcription of the audio
    """
    r = sr.Recognizer()
    output = '/tmp/out_test.wav'
    sound = AudioSegment.from_mp3(audio_path)
    sound.export(output, format="wav")
    with sr.AudioFile(output) as source:
        audio = r.record(source)
        # We use the standard speech
        # recognition system from google here.
        # You can switch this by changing
        # it in the next line
        return r.recognize_google(audio)


def text_to_text(text):
    """Sends a request as text to pepper, and
    returns the answer of the AVS in Textform

    Args:
        text (string): The request for avs

    Returns:
        the answer of avs to the given request
    """
    global alexa
    alexa = AlexaClient()
    return audio_to_text(text_to_audio(text))


def main():
    global alexa
    alexa = AlexaClient()
    print "Type 'quit' to exit"
    quit = False
    while not quit:
        text = raw_input("Command to send to Alexa: ")

        if text == 'quit':
            quit = True
        else:
            print text_to_text(text)
            # Uncomment this if you want the response also as audio
            # play_mp3(audio_response)


if __name__ == '__main__':
    main()
