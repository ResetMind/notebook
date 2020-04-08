import json
from requests import get, post


key = "trnsl.1.1.20200407T174223Z.422d3fccca45d937.5e142ba7e77ce7d8739ef8b08f096a2fad5f9bcf"


def translate(text, source_language, dest_language):
    if source_language == 'auto':
        params = {
            "key": key,
            "text": text,
            "lang": dest_language
        }
    else:
        params = {
            "key": key,
            "text": text,
            "lang": source_language + "-" + dest_language
        }
    response = get("https://translate.yandex.net/api/v1.5/tr.json/translate", params=params)
    print(response.status_code)
    if response.status_code == 401:
        return 'Invalid API Key'
    elif response.status_code == 402:
        return 'API key is locked'
    elif response.status_code == 404:
        return 'The daily limit on the amount of translated text has been exceeded'
    elif response.status_code == 413:
        return 'Maximum text size exceeded'
    elif response.status_code == 422:
        return 'Text cannot be translated'
    elif response.status_code == 501:
        return 'The specified translation direction is not supported'
    elif response.status_code != 200:
        return 'Translation error'
    data = json.loads(response.content.decode('utf-8-sig'))
    return data['text'][0]
