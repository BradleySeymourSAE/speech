import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
speech = sr.Recognizer()
# Reading Microphone as source
# listening the speech and store in audio_text variable

with sr.Microphone() as source:
    print("Microphone has started listening to your audio input")
    audio_text = speech.listen(source)
    print("Microphone has stopped listening for input, please wait while we transcribe the audio to text")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        print("SUCCESS\nTranscription Text: "+speech.recognize_google(audio_text))
    except:
         print("FAILED\nSorry, I couldn't quite understand what was being said, please remove any background noise or adjust your microphone settings.")