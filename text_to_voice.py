#! /bin/python3
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("GQ_jXbMni0t65aKSG_wputCEPVkss2bySXPVY8eizs0d")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/0bf06db1-a81d-478b-b6f3-74308b6c0644")
with open("demo.txt") as text_file:
    data = text_file.read()
    text_file.close()
with open("demo2.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize(data,accept="audio/mp3").get_result().content
    )
