from numpy import record
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import urllib.request
import re
import json
import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("popup.html", {"request": request})

@app.post("/summarize")
def perform_summary(youtube_video:str):
    video_id = youtube_video.split("=")[1]
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    result = ""
    for i in transcript:
        result += ' ' + i['text']
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
    summarized_text = summarizer(result, min_length=5, max_length=100)
    text = summarized_text[0]['summary_text']
    v = pd.DataFrame([text], columns=['summary'])
    return json.loads(v.to_json(orient='records'))[0]