def triage_text(texto: str):
    texto = texto.lower()

    sintomas_avc = [
        "fala enrolada",
        "fraqueza",
        "dormência",
        "lado esquerdo",
        "lado direito"
    ]

    sintomas_infarto = [
        "dor no peito",
        "aperto no peito",
        "falta de ar",
        "suor frio",
        "náusea"
    ]

    risco_avc = any(s in texto for s in sintomas_avc)
    risco_infarto = any(s in texto for s in sintomas_infarto)

    if risco_avc:
        return {
            "risco": "ALTO",
            "condicao": "AVC",
            "orientacao": "Emergência imediata (192)."
        }

    if risco_infarto:
        return {
            "risco": "ALTO",
            "condicao": "INFARTO",
            "orientacao": "Emergência imediata."
        }

    return {
        "risco": "BAIXO",
        "condicao": "INDEFINIDO",
        "orientacao": "Observe sintomas e procure médico se persistirem."
    }

