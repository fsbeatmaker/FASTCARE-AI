import re

# Sintomas críticos para triagem preventiva
CRITICAL_SYMPTOMS = {
    "avc": [
        "boca paralisada",
        "fala enrolada",
        "fala arrastada",
        "braço dormente",
        "perna dormente",
        "fraqueza em um lado",
        "formigamento",
        "visão embaçada",
        "confusão mental"
    ],
    "infarto": [
        "dor no peito",
        "aperto no peito",
        "dor forte no peito",
        "falta de ar",
        "suor frio",
        "náusea",
        "tontura",
        "dor no braço esquerdo"
    ],
    "geral": [
        "estou morrendo",
        "mal súbito",
        "desmaio",
        "dor intensa"
    ]
}

NEGATIONS = ["não", "sem", "nenhuma", "nunca"]


def is_negated(text: str, symptom: str) -> bool:
    """
    Verifica se o sintoma está negado (ex: 'não estou com dor no peito')
    """
    pattern = rf"(?:{'|'.join(NEGATIONS)})\s+(?:\w+\s+){{0,3}}{symptom}"
    return re.search(pattern, text) is not None


def analyze_text(text: str) -> dict:
    text = text.lower()

    score = 0
    matched_symptoms = []

    for _, symptoms in CRITICAL_SYMPTOMS.items():
        for symptom in symptoms:
            if re.search(symptom, text):
                if not is_negated(text, symptom):
                    score += 3
                    matched_symptoms.append(symptom)

    # Classificação de risco (triagem conservadora)
    if score >= 6:
        risk_level = "alto"
    elif score >= 3:
        risk_level = "moderado"
    else:
        risk_level = "baixo"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "matched_symptoms": matched_symptoms,
        "recommendation": generate_recommendation(risk_level)
    }


def generate_recommendation(risk_level: str) -> str:
    if risk_level == "alto":
        return (
            "⚠️ RISCO ALTO detectado. "
            "Procure atendimento médico imediato ou ligue para o SAMU (192)."
        )
    elif risk_level == "moderado":
        return (
            "⚠️ RISCO MODERADO. "
            "Recomenda-se avaliação médica o quanto antes ou ligue para o SAMU (192)."
        )
    else:
        return (
            "✅ RISCO BAIXO no momento. "
            "Continue monitorando os sintomas."
        )
