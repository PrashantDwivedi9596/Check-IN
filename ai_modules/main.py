from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn
from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import os
from datetime import datetime
import json

app = FastAPI()

# Initialize Whisper model
model = WhisperModel("base", device="cpu", compute_type="int8")

class AudioInput(BaseModel):
    audio_data: list[float]
    sample_rate: int

class TranscriptionResponse(BaseModel):
    text: str
    segments: list[dict]
    language: str

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_audio(audio: AudioInput):
    try:
        # Convert audio data to numpy array
        audio_array = np.array(audio.audio_data, dtype=np.float32)
        
        # Save temporary audio file
        temp_file = f"temp_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        write(temp_file, audio.sample_rate, audio_array)
        
        # Transcribe audio
        segments, info = model.transcribe(temp_file, beam_size=5)
        
        # Process segments
        text = ""
        segment_list = []
        for segment in segments:
            text += segment.text + " "
            segment_list.append({
                "start": segment.start,
                "end": segment.end,
                "text": segment.text
            })
        
        # Clean up temporary file
        os.remove(temp_file)
        
        return TranscriptionResponse(
            text=text.strip(),
            segments=segment_list,
            language=info.language
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 