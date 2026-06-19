# Azure Speech Services

Bidirectional speech pipeline using **Azure Cognitive Services – Speech SDK**:

- **Speech-to-text**: captures one utterance from the default microphone
- **Text-to-speech**: synthesizes the transcription back to audio and plays it via VLC

## Prerequisites

- Python 3.8+
- An active **Azure Cognitive Services – Speech** resource
- A working microphone
- **VLC** media player installed (`vlc` available on `PATH`) for audio playback

> ⚠️ **Azure dependency**: all environment variable values are placeholders. Replace them with your actual Azure resource credentials before running.

## Setup

```bash
git clone https://github.com/<your-username>/azure-speech-services.git
cd azure-speech-services

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# Edit .env with your credentials
```

## Environment Variables

| Variable              | Description                                                    | Default          |
|-----------------------|----------------------------------------------------------------|------------------|
| `AZURE_SPEECH_KEY`    | API key for the Azure Speech resource                          | *(required)*     |
| `AZURE_SPEECH_REGION` | Azure region (e.g. `westeurope`)                               | *(required)*     |
| `AZ_SPEECH_LANGUAGE`  | BCP-47 language code for recognition (e.g. `it-IT`, `en-US`)  | `it-IT`          |
| `AZ_SPEECH_VOICE`     | Neural voice name for synthesis                                | `it-IT-IsabellaNeural` |

## Usage

```bash
python main.py
```

The script listens once from the microphone, prints the transcription with its duration in ticks, then synthesizes and plays back a confirmation phrase.

## Notes

- The output audio is saved to `output.wav` in the working directory.
- VLC must be installed and accessible via the system `PATH`. Alternatively, replace `play_audio_file()` with any player of your choice.

## Project Structure

```
azure-speech-services/
├── main.py
├── requirements.txt
├── .env.example
└── .gitignore
```

## License

MIT
