import os
from google.cloud import texttospeech
from optparse import OptionParser

# Parse command line options
parser = OptionParser()
parser.add_option("-f", "--file", dest="file",
                  help="txt file with the text to synthesize", metavar="FILE")
parser.add_option("-c", "--credentials", dest="credentials",
                  help="The JSON file that contains your service account key",
                  metavar="KEY")
(options, args) = parser.parse_args()

# check if all options are set
if options.file is None or options.credentials is None:
    parser.error("""Missing one or more required options: -f, -c
Use: text2speech.py -h for help""")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = options.credentials

# create string from file
with open(options.file, 'r', encoding='utf-8') as f:
    inputtext = f.read()

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text=inputtext)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    name='en-US-Wavenet-D',
    language_code="en-US",
    ssml_gender=texttospeech.SsmlVoiceGender.MALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
