import requests


def translate_text(text, target_language):
    url = "https://intelligence.kritrimaprajna.com//api/v1/text/translate/single"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "to_language": target_language
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data['data']['translated_text']
    else:
        return text
    
