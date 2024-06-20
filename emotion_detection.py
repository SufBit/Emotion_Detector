import requests
import json


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        json_data = response.json()
        emotion_pred = json_data.get('emotionPredictions', [])
        extracted_emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

        if emotion_pred:
            ex_emotions = emotion_pred[0].get('emotion', {})
            for i in extracted_emotions.keys():
                if i in ex_emotions:
                    extracted_emotions[i] = ex_emotions[i]

            dominant_emotion = max(ex_emotions, key=ex_emotions.get)
            extracted_emotions['dominant_emotion'] = dominant_emotion
        
        return extracted_emotions

