import json
import requests
from app import app
from requests import get, post


key = "trnsl.1.1.20200407T174223Z.422d3fccca45d937.5e142ba7e77ce7d8739ef8b08f096a2fad5f9bcf"


def translate(text, source_language, dest_language):
    params = {
        "key": key,
        "text": text,
        "lang": source_language + "-" + dest_language
    }
    response = get("https://translate.yandex.net/api/v1.5/tr.json/translate", params=params)
    r_json = response.json()
    if response.status_code != 200:
        return 'Error: the translation service failed.'
    data = json.loads(response.content.decode('utf-8-sig'))
    return data['text'][0]
