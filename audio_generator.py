import requests

languages=[
        {
            "_id": "688d15df841e4bb3d1f58b24",
            "language_id": "default",
            "language_name": "English (India)",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "English (India) voice — en-IN-NeerjaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"en-US\"><voice name=\"en-IN-NeerjaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "en",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b25",
            "language_id": "hindi",
            "language_name": "Hindi",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Hindi voice — hi-IN-AnanyaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"hi-IN\"><voice name=\"hi-IN-AnanyaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "hi",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b26",
            "language_id": "marathi",
            "language_name": "Marathi",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Marathi voice — mr-IN-AarohiNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"mr-IN\"><voice name=\"mr-IN-AarohiNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "mr",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b27",
            "language_id": "french",
            "language_name": "French",
            "language_icon_link": "https://flagcdn.com/w2560/fr.png",
            "language_description": "French voice — fr-FR-BrigitteNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"fr-FR\"><voice name=\"fr-FR-BrigitteNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "fr",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b28",
            "language_id": "spanish",
            "language_name": "Spanish",
            "language_icon_link": "https://flagcdn.com/w2560/es.png",
            "language_description": "Spanish voice — es-ES-AbrilNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"es-ES\"><voice name=\"es-ES-AbrilNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "es",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b29",
            "language_id": "italian",
            "language_name": "Italian",
            "language_icon_link": "https://flagcdn.com/w2560/it.png",
            "language_description": "Italian voice — it-IT-IsabellaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"it-IT\"><voice name=\"it-IT-IsabellaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "it",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2a",
            "language_id": "chinese",
            "language_name": "Chinese (Traditional)",
            "language_icon_link": "https://flagcdn.com/w2560/tw.png",
            "language_description": "Chinese (Traditional) voice — zh-TW-HsiaoYuNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"zh-TW\"><voice name=\"zh-TW-HsiaoYuNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "zh-CN",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2b",
            "language_id": "swahili",
            "language_name": "Swahili",
            "language_icon_link": "https://flagcdn.com/w2560/ke.png",
            "language_description": "Swahili voice — sw-KE-ZuriNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"sw-KE\"><voice name=\"sw-KE-ZuriNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "sw",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2c",
            "language_id": "vietnamese",
            "language_name": "Vietnamese",
            "language_icon_link": "https://flagcdn.com/w2560/vn.png",
            "language_description": "Vietnamese voice — vi-VN-HoaiMyNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"vi-VN\"><voice name=\"vi-VN-HoaiMyNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "vi",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2d",
            "language_id": "tamil",
            "language_name": "Tamil",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Tamil voice — ta-IN-PallaviNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"ta-IN\"><voice name=\"ta-IN-PallaviNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "ta",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2e",
            "language_id": "telugu",
            "language_name": "Telugu",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Telugu voice — te-IN-ShrutiNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"te-IN\"><voice name=\"te-IN-ShrutiNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "te",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "portuguese",
            "language_name": "Portuguese",
            "language_icon_link": "https://flagcdn.com/w2560/br.png",
            "language_description": "Portuguese voice — pt-BR-BrendaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"pt-BR\"><voice name=\"pt-BR-BrendaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "pt",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "arabic",
            "language_name": "Arabic",
            "language_icon_link": "https://flagcdn.com/w2560/ae.png",
            "language_description": "Arabic voice — ar-AE-FatimaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"ar-AE\"><voice name=\"ar-AE-FatimaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "ar",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "indonesian",
            "language_name": "Indonesian",
            "language_icon_link": "https://flagcdn.com/w2560/id.png",
            "language_description": "Indonesian voice — id-ID-GadisNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"id-ID\"><voice name=\"id-ID-GadisNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "id",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "urdu",
            "language_name": "Urdu",
            "language_icon_link": "https://flagcdn.com/w2560/pk.png",
            "language_description": "Urdu voice — ur-IN-AishaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"ur-IN\"><voice name=\"ur-IN-SalmanNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "ur",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "gujarati",
            "language_name": "Gujarati",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Gujarati voice — gu-IN-DhwaniNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"gu-IN\"><voice name=\"gu-IN-DhwaniNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "gu",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"
        },
        {
            "_id": "688d15df841e4bb3d1f58b2f",
            "language_id": "bangla",
            "language_name": "Bengali",
            "language_icon_link": "https://flagcdn.com/w2560/in.png",
            "language_description": "Bengali voice — bn-IN-TanishaaNeural",
            "language_ssml": "<speak xmlns=\"http://www.w3.org/2001/10/synthesis\" xmlns:mstts=\"http://www.w3.org/2001/mstts\" xmlns:emo=\"http://www.w3.org/2009/10/emotionml\" version=\"1.0\" xml:lang=\"bn-BD\"><voice name=\"bn-BD-NabanitaNeural\"><prosody rate=\"0%\" pitch=\"0%\">",
            "language_code": "bn",
            "created_at": "1750350600000",
            "user_id": "001329.d54007cf2bbc44f5ac86df4e9c28f027.0951"

        }
    ]

def getSSMLFromLanguageCode(language_code):
    for lang in languages:
        if lang['language_code'] == language_code:
            return lang['language_ssml']
    return None

def generate_audio(text, target_language):
    try:
        SSML = getSSMLFromLanguageCode(target_language)
        if not SSML:
            print(f"SSML not found for language code: {target_language}")
            return "none"

        url = "https://intelligence.kritrimaprajna.com/api/v1/audio/text-to-audio"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "text": text,
            "SSML": SSML
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data['data']['file_url']
        else:
            return "none"
    except:
        return "none"
    



print(generate_audio("Hello, how are you?", "hi"))