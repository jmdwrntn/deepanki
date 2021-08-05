import requests
import json
import os
from dotenv import load_dotenv


# DeepL API auth key stored in .env
load_dotenv()


class Connection():

    def __init__(self):
        super().__init__()

        self.translate
        self.request
        self.invoke

    def translate(self, text, language):
        # Arguements for API auth key,
        # text for translation and target language
        url = 'https://api-free.deepl.com/v2/translate?'
        data = {'auth_key': os.environ['AUTH_KEY'],
                'text': text,
                'target_lang': language}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        # Post request to API with above arguements
        response = requests.post(url, data, headers)

        # Convert response to JSON
        jsonResponse = response.json()

        # Return the translated text
        return(jsonResponse["translations"][0]["text"])

    @staticmethod
    def request(action, **params):
        return {'action': action, 'params': params, 'version': 6}

    @staticmethod
    def invoke(action, **params):
        requestJson = json.dumps(
            Connection.request(action, **params)
            ).encode('utf-8')
        response = requests.post('http://localhost:8765', requestJson)
        jsonResponse = response.json()

        if len(jsonResponse) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in jsonResponse:
            raise Exception('response is missing required error field')
        if 'result' not in jsonResponse:
            raise Exception('response is missing required result field')
        if jsonResponse['error'] is not None:
            raise Exception(jsonResponse['error'])
        return jsonResponse['result']
