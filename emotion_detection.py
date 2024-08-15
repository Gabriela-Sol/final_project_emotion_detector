"""
Module for detecting emotions using an external API.
"""

import json
import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using the Watson NLP Emotion API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        The response from the emotion detection API as a dictionary with emotion scores and the dominant emotion.
    """
    # Define the URL for the emotion detection API
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/'
        'NlpService/EmotionPredict'
    )

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    formatted_response = json.loads(response.text)

    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

    emotion_scores = {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    return emotion_scores

