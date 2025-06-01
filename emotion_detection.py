import json
import requests

def sentiment_analyzer(text_to_analyse):
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    text  = requests.post(url, json=myobj, headers=header, timeout=30)
    return text
