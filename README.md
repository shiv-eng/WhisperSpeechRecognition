```
# **Speech Recognition Web App**

## **Description**

This is a Flask web application that utilizes the OpenAI Whisper ASR API for speech recognition. Users can record their speech, and the application transcribes the audio content, storing the results in a local SQLite database. The application supports both English and Hindi languages.

## **Getting Started**

### **Prerequisites**

- Python 3.6 or higher
- Pip (package installer for Python)

### **Installation**

1. **Clone the repository:**

 
   git clone https://github.com/your-username/speech-recognition-web-app.git
   cd speech-recognition-web-app
   

2. **Install dependencies:**


   pip install -r requirements.txt

3. **Run the application:**

 
   python app.py
  

## **Usage**

1. Open the web application in your browser: [http://localhost:5000](http://localhost:5000)
2. Click on "**Start Recording**" to begin speech recognition.
3. Speak into your microphone.
4. Click on "**Stop Recording**" to end the recording.
5. Refresh the page to view recorded notes.

## **Features**

- **Speech Recognition:**
  - Utilizes OpenAI Whisper ASR API for accurate speech recognition.
- **Multi-Language Support:**
  - Supports both English and Hindi languages.
- **Database Storage:**
  - Stores transcribed notes in a local SQLite database.

## **Contributing**

If you would like to contribute to the project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Make changes and commit them: `git commit -m "Your message"`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## **Acknowledgements**

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://www.openai.com/)
- [SQLite](https://www.sqlite.org/)

