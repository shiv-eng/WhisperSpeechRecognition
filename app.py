from flask import Flask, render_template, request, jsonify
from datetime import datetime
import sqlite3
import openai
import os

app = Flask(__name__)


# Function to connect to the database
def connect_db():
    db_path = os.path.join(os.path.dirname(__file__), 'notes.db')
    return sqlite3.connect(db_path)


# Function to create the notes table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            timestamp DATETIME
        )
    ''')
    conn.commit()
    conn.close()


# Set your OpenAI API key
OPENAI_API_KEY = 'your_api_key'
openai.api_key = OPENAI_API_KEY


def recognize_speech(audio_content, language_code='en'):
    model = "whisper-large" if language_code == 'en' else "whisper-large-non-english"

    response = openai.TextCompletion.create(
        model=model,
        prompt=audio_content,
        temperature=0.5,
        max_tokens=200
    )

    return response['choices'][0]['text'].strip()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recognize', methods=['POST'])
def recognize_whisper_speech():
    try:
        create_table()

        audio_content = request.data.decode('utf-8')
        language_code = request.headers.get('Content-Language', 'en')  # Default to English if not provided

        # Use OpenAI Whisper ASR API for speech recognition
        text = recognize_speech(audio_content, language_code)

        # Save the note to the database with a timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO notes (text, timestamp) VALUES (?, ?)', (text, timestamp))
        conn.commit()
        conn.close()

        print(f"Speech Recognized: {text} - {timestamp}")

        return jsonify({'status': 'success', 'text': text, 'timestamp': timestamp})

    except Exception as e:
        print(f"Error during speech recognition: {e}")
        return jsonify({'status': 'error', 'message': f"Error during speech recognition; {e}"})


@app.route('/get_notes')
def get_notes():
    try:
        create_table()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM notes ORDER BY timestamp DESC')
        notes = cursor.fetchall()
        conn.close()
        return jsonify({'notes': notes})

    except Exception as e:
        print(f"Error fetching notes: {e}")
        return jsonify({'status': 'error', 'message': f"Error fetching notes; {e}"})


if __name__ == '__main__':
    app.run(debug=True)
