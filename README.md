# Google Text to Speech Client

A Python script used to convert text to speech using Google Text-to-Speech/Wavenet
Please note:

- This script uses WaveNet, this will allow you to synthesize 1.000.000 characters every month, synthesizing more will cost you money
- This Client is limited to 5000 characters per request.

## Prerequisites

- You have access to a GCP project
- You've [set up authentication](https://cloud.google.com/text-to-speech/docs/libraries#setting_up_authentication)

## Usage

Clone the repository:

```bash
git clone https://github.com/thijsvanloef/Google-Text-to-Speech-Client`
```

Install the Client Library:

```bash
pip install --upgrade google-cloud-texttospeech
```

Run the script:

```bash
python3 text2speech -f <textfile> -c <service_account.json>
```

This will generate an `output.mp3`.
