from fastapi import FastAPI
app = FastAPI()

from pydantic import BaseModel
import shutil
import os

from ia_triagem_avc_infarto.audio_analysis import analyze_audio
from ia_triagem_avc_infarto.text_analysis import analyze_text
from ia_triagem_avc_infarto.models.risk_model import calculate_risk

# ===============================
# CHATBOT
# ===============================
from ia_triagem_avc_infarto.services.chatbot_service import chat_with_llm

@app.get("/")
def root():
    return {"status": "FastCare AI online"}

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/api", methods=["POST"])
def chat():
    return jsonify({"reply": "funcionando"})

# ===============================
# MODELOS
# ===============================
class TextRequest(BaseModel):
    text: str
    idade: int | None = None
    sexo: str | None = None

# ===============================
# ENDPOINT TEXTO (JSON)
# ===============================
@app.post("/triage/text")
def triage_text(data: TextRequest):
    text_features = analyze_text(data.text)

    resultado = calculate_risk(
        audio_features=None,  # sem áudio
        text_features=text_features,
        idade=data.idade,
        sexo=data.sexo
    )

    return {
        "resultado": resultado,
        "text_features": text_features
    }

# ===============================
# ENDPOINT TEXTO (FORM)
# ===============================
@app.post("/triagem/texto")
def triagem_texto(
    texto: str = Form(...),
    idade: int | None = Form(None),
    sexo: str | None = Form(None)
):
    text_features = analyze_text(texto)

    resultado = calculate_risk(
        audio_features=None,
        text_features=text_features,
        idade=idade,
        sexo=sexo
    )

    return {
        "resultado": resultado,
        "text_features": text_features
    }

# ===============================
# ENDPOINT AUDIO
# ===============================
@app.post("/triagem/audio")
def triagem_audio(audio: UploadFile = File(...)):
    audio_path = f"temp_{audio.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    audio_features = analyze_audio(audio_path)
    os.remove(audio_path)

    return audio_features

# ===============================
# ENDPOINT COMPLETO (TEXTO + ÁUDIO)
# ===============================
@app.post("/triagem")
def triagem(
    audio: UploadFile = File(...),
    texto: str = Form(...),
    idade: int | None = Form(None),
    sexo: str | None = Form(None)
):
    audio_path = f"temp_{audio.filename}"

    with open(audio_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    audio_features = analyze_audio(audio_path)
    text_features = analyze_text(texto)

    os.remove(audio_path)

    resultado = calculate_risk(
        audio_features=audio_features,
        text_features=text_features,
        idade=idade,
        sexo=sexo
    )

    return {
        "resultado": resultado,
        "audio_features": audio_features,
        "text_features": text_features
    }

# ===============================
# ENDPOINT CHATBOT
# ===============================
@app.post("/chat")
def chat(prompt: str = Form(...)):
    return chat_with_llm(prompt)



    return response.json()
