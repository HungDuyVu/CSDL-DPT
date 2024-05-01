import speech_recognition as sr
from pydub import AudioSegment
from database import db

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the MP3 audio file
mp3_audio_file = "audio/1_PresidentTrumpandTheFirstLadyAttendtheGovernorsBallmpmp.mp3"
wav_audio_file = "converted_audio.wav"

# Convert MP3 to WAV
audio = AudioSegment.from_mp3(mp3_audio_file)
audio.export(wav_audio_file, format="wav")
print('start')
# Use the recognizer to open the WAV audio file
with sr.AudioFile(wav_audio_file) as source:
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    
    # Listen to the audio file and store the audio data in 'audio'
    audio = recognizer.record(source)

    try:
        # Use the recognizer to convert speech to text
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)
        db.save_word_extraction(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
