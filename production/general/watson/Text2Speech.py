
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# Dub
import pygame

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

#apiKey = ""
#runIBMTextToSpeech("sampleText.txt",apiKey,"closeAchievement.wav",'en-US_AllisonExpressive')    

class Text2Speech():
      
    def __init__(self, key: str, url: str):
        """
        General text 2 epssh object
        """
        self.AUDIO_FILE_PATH = "graphics/audio/text2speech.wav"

        self.api_key = key
        self.url = url
        self.authenticator = IAMAuthenticator(self.api_key)
        self.t2s_agent = TextToSpeechV1( authenticator=self.authenticator)
        self.t2s_agent.set_service_url(self.url)
        
        self.is_synthesizing = False
    
    def synthesize_by_str(self, text: str):
        """
        synthesize the speech. it will overwrite the content of the audio file
        """
        with open(self.AUDIO_FILE_PATH, 'wb') as audio_file:
            self.is_synthesizing = True
            audio_file.write(
                self.t2s_agent.synthesize(
                text,
                accept='audio/wav'
                ).get_result().content)

        self.is_synthesizing = False
    
    def synthesize_by_file(self, text_file_path):

        watsonTextFile = open(text_file_path,"r")
        watsonText = watsonTextFile.read()
        watsonTextFile.close()

        self.synthesize_by_str(watsonText)

    def play(self, channel_number: int):
        """
        play the audio using pygame mixer,
        you may want to specify the mixer channel so it doesnt clash with other audio 
        """
        pygame.mixer.Channel(channel_number).play(pygame.mixer.Sound(self.AUDIO_FILE_PATH))
    
            
    
# song = AudioSegment.from_wav('closeAchievement.wav')
# play(song)
