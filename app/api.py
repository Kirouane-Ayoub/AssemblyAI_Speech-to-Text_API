from fastapi import FastAPI, UploadFile, File
import assemblyai as aai
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

aai.settings.api_key = ""
transcriber = aai.Transcriber()

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        # Check if a file was provided
        if not file:
            return {"error": "No file provided"}

        # Save the audio file locally
        audio_path = "audio.mp3"
        with open(audio_path, "wb") as audio_file:
            audio_file.write(await file.read())

        # Perform transcription using AssemblyAI
        transcript = transcriber.transcribe(audio_path)

        # Return the transcript
        return {"transcript": transcript.text}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
