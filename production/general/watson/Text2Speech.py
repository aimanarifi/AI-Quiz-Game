import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Dub
from pydub import AudioSegment
from pydub.playback import play


"""
 textFilePath : String
 apiKey : String
 fileName : String 
 voice : String 
 

"""

def runIBMTextToSpeech(textFilePath, apiKey, filename , aiVoice ):
        watsonTextFile = open(textFilePath,"r")
        watsonText = watsonTextFile.read()
        watsonTextFile.close()

        authenticator = IAMAuthenticator(apiKey)
        text_to_speech = TextToSpeechV1(
            authenticator=authenticator
        )

        text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/2340778d-f272-4d32-bf19-1d83f9ad9a0d')

        with open(filename, 'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    watsonText,
                    voice=aiVoice,
                    accept='audio/wav'        
                ).get_result().content) 
    
    
# Parameter: (textFilePath, yourAPIKey, filename, voiceType)    

apiKey = ""
runIBMTextToSpeech("sampleText.txt",apiKey,"closeAchievement.wav",'en-US_AllisonExpressive')    
    
    
    
    
    
    
# song = AudioSegment.from_wav('closeAchievement.wav')
# play(song)
