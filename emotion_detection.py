"""
Module for detecting emotions using an external API.
"""

import requests

def emotion_detector(text_to_analyze):
    """
    Detects emotions in the provided text using the Watson NLP Emotion API.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        str: The response from the emotion detection API.
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

    return response.text
