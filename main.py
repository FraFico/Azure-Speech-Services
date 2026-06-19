"""
main.py – Azure Speech Services
────────────────────────────────
Speech-to-text from the default microphone, then text-to-speech
output saved to a .wav file and played back via VLC.
"""

import os
import sys
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

# Global config object shared by all functions
config: speechsdk.SpeechConfig = None


def speech_to_text() -> tuple[str, int]:
    """Capture one utterance from the default microphone and return (text, duration)."""
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    recognizer = speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio_config)

    print("Sto ascoltando...")
    result = recognizer.recognize_once_async().get()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        return result.text, result.duration
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Nessun discorso riconosciuto")
        sys.exit(1)
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Cancellato: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error: {cancellation_details.error_details}")
        raise RuntimeError(
            f"Errore durante il riconoscimento vocale. {cancellation_details.error_details}"
        )


def text_to_speech(text: str, output_file: str = "output.wav") -> str:
    """Synthesize text to speech and save to a .wav file."""
    audio_config = speechsdk.audio.AudioOutputConfig(filename=output_file)
    syntetizer = speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_config)

    result = syntetizer.speak_text_async(text).get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        play_audio_file(output_file)
        return "done"
    else:
        return "fail"


def play_audio_file(filename: str = "output.wav") -> None:
    """Play a .wav file using VLC (must be installed on the system)."""
    os.system(f"vlc {filename}")


def main() -> None:
    global config
    load_dotenv()

    key = os.getenv("AZURE_SPEECH_KEY")
    region = os.getenv("AZURE_SPEECH_REGION")

    config = speechsdk.SpeechConfig(subscription=key, region=region)
    config.speech_recognition_language = os.getenv("AZ_SPEECH_LANGUAGE") or "it-IT"
    config.speech_synthesis_voice_name = os.getenv("AZ_SPEECH_VOICE") or "it-IT-IsabellaNeural"

    testo, durata = speech_to_text()
    print(f"Ho capito ({durata} ticks): {testo}")
    text_to_speech(f"Hai detto: {testo}?")


if __name__ == "__main__":
    main()
