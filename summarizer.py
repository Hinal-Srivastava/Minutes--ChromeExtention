from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo
import urllib.request
import json
import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("popup.html")

@app.route("/result")
def result():
    output = request.form.to_dict()
    url = output["url"]
    return render_template("popup.html")

@app.route("/summarizer")
def summarizer(url):
    video_id = url.split("=")[1]
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarized_text = summarizer(result, min_length=5, max_length=100)
    text = summarized_text[0]['summary_text']
    return 'Text Summarized'


if __name__=='__main__':
    app.run(debug=True)

