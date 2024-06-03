# translator.py

from googletrans import Translator

def translate_text(text, source_language='auto', target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, src=source_language, dest=target_language)
    return translated_text.text
