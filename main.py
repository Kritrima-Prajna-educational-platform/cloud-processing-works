from email.mime import audio
from email.policy import default
from translate import translate_text
import json
from audio_generator import generate_audio

with open('./innovator.lessons.json', 'r', encoding='utf-8') as infile:
    lessons = json.load(infile)

language_to_translate = {
    "hindi": "hi",
    "marathi": "mr",
    "tamil": "ta",
    "telugu": "te",
    "french": "fr",
    "spanish": "es",
    "italian": "it",
    "swahili": "sw",
    "chinese": "zh-CN",
    "portuguese": "pt",
    "vietnamese": "vi",
    "english": "en",
    "default": "en",
}

keys_to_translate = ['circuitInstructions', 'codeInstructions', "iotInstructions"]
lesson_number=0
print(f"Total Lessons: {len(lessons)}")
for lesson in lessons:
    print(lesson['name'])
    for key in keys_to_translate:
        if key in lesson:
            print(f"  Translating {key}...")
            for language in language_to_translate.keys():
                # print(lesson[key]['content'], key)
                # if(len(lesson[key]['content'].keys())>1):
                #     lesson[key]['content'][language] = lesson[key]['content']['default']
                if language in lesson[key]['content']:
                    index=0
                    for step in lesson[key]['content'][language]:
                        print(f"      Step [{index}]: {step['description']}")
                        language_code = language_to_translate[language]
                        translated_text = translate_text(step['description'], target_language=language_code)
                        audio_url = generate_audio(translated_text, target_language=language_code)
                        # translated_text = lesson[key]['content']['default'][index]['description']
                        print(f"      Translated [{language}]: {translated_text}")
                        print(f"      Audio URL [{language}]: {audio_url}")
                        lesson[key]['content'][language][index]['description'] = translated_text
                        lesson[key]['content'][language][index]['audio'] = audio_url
                        index += 1
    print(f"Completed Lesson {lesson_number}\n")
    lesson_number += 1
print("All Lessons Completed")
with open('./updated.json', 'w', encoding='utf-8') as outfile:
    json.dump(lessons, outfile, ensure_ascii=False, indent=4)