from audio_analysis import analyze_audio
from ia_triagem_avc_infarto.text_analysis import analyze_text
from ia_triagem_avc_infarto.models.risk_model import calculate_risk

audio_path = "teste2.wav"  # coloque um áudio real aqui
text = "Hoje estou me sentindo estranho e tô com dificuldade de falar."

audio_features = analyze_audio(audio_path)
text_features = analyze_text(text)

resultado = calculate_risk(audio_features, text_features)

print(resultado)

