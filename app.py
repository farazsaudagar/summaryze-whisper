from flask import Flask, request
from flask_cors import CORS, cross_origin
import pandas as pd
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import openai as ai
import os
load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

ai.api_key = os.getenv('OPENAI_API_KEY')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        youtube_url = request.data.decode('utf-8')
        transcript_list = YouTubeTranscriptApi.list_transcripts(
            youtube_url.split('=')[1])

        transcript = transcript_list.find_generated_transcript(['en']).fetch()
        formatter = TextFormatter()
        json_formatted_text = formatter.format_transcript(
            transcript=transcript)
        print(json_formatted_text)
        # completions = ai.Completion.create(
        #     engine='text-davinci-003',
        #     temperature=0.5,
        #     prompt=f"Generate summary notes based on this YouTube transcript here: {json_formatted_text}",
        #     max_tokens=100,
        #     n=1,
        # )
        # print(completions)
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
