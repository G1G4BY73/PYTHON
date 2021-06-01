#! /bin/python3
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("AvAZvgleMOnj58SZigmGS2o8ecHQNr4PxrIbhiilO0r7")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/250118a0-ab90-4616-8888-e7065d28fdeb")
with open("demo.txt") as text_file:
    data = text_file.read()
    text_file.close()
with open("demo8.mp3","wb") as audiofile:
    audiofile.write(
    text_2_speech.synthesize(data,accept="audio/mp3").get_result().content
    )
