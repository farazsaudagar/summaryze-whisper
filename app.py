from flask import Flask, request
from flask_cors import CORS, cross_origin
from pytube import YouTube
import whisper
import pandas as pd

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.data.decode('utf-8')
        print(youtube_url)
        audio_file = YouTube(youtube_url).streams.filter(
            only_audio=True).first().download(filename="audio.mp4")
        whisper_model = whisper.load_model("tiny")
        transcription = whisper_model.transcribe(audio_file)
        df = pd.DataFrame(transcription['segments'], columns=[
                          'start', 'end', 'text'])
        print(df)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
