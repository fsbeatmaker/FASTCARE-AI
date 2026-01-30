import librosa
import numpy as np
import tempfile

def triage_audio(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_file.file.read())
        tmp_path = tmp.name

    y, sr = librosa.load(tmp_path, sr=None)

    energia = np.mean(librosa.feature.rms(y=y))

    if energia < 0.01:
        return {
            "risco": "MODERADO",
            "observacao": "Fala muito fraca ou arrastada detectada",
            "orientacao": "Se houver outros sintomas, procure emergência"
        }

    return {
        "risco": "BAIXO",
        "observacao": "Padrão de voz dentro do esperado",
        "orientacao": "Nenhum sinal crítico detectado"
    }

