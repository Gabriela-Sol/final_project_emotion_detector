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
        The response from the emotion detection API as a dictionary 
        with emotion scores and the dominant emotion.
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

    # Check if the response status code indicates an error
    if response.status_code == 400:
        return {
            emotion: None
            for emotion in ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']
            }

    # Extract emotion scores from the response
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_scores = {
        emotion: formatted_response['emotionPredictions'][0]['emotion'].get(emotion, 0)
        for emotion in emotions
    }

    emotion_scores['dominant_emotion'] = max(emotion_scores, key=emotion_scores.get)

    return emotion_scores
