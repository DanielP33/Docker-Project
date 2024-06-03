# app.py

from flask import Flask, request, jsonify, render_template
from translator import translate_text  # Import the translate_text function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    source_lang = data.get('source_lang', 'auto')  # Default source language is auto
    target_lang = data.get('target_lang', 'en')    # Default target language is English

    if not text:
        return jsonify({'error': 'Text to translate is required.'}), 400

    translated_text = translate_text(text, source_lang, target_lang)  # Call translate_text function
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
