def calculate_risk(
    audio_features: dict,
    text_features: dict,
    idade: int | None = None,
    sexo: str | None = None
) -> dict:
    score = 0
    fatores = []

    # -----------------------
    # 🎙️ ÁUDIO
    # -----------------------
    if audio_features:
        if audio_features.get("tempo", 120) < 90:
            score += 2
            fatores.append("fala lenta ou alterada")

        if audio_features.get("zcr", 0.1) < 0.05:
            score += 2
            fatores.append("padrão vocal anormal")

    # -----------------------
    # 📝 TEXTO (peso maior)
    # -----------------------
    text_score = text_features.get("risk_score", 0)
    score += text_score
    if text_score >= 3:
        fatores.append("sintomas críticos relatados")

    # -----------------------
    # 🎂 IDADE
    # -----------------------
    if idade:
        if idade >= 60:
            score += 2
            fatores.append("idade elevada (≥60)")
        elif idade >= 45:
            score += 1
            fatores.append("idade intermediária")

    # -----------------------
    # ⚧️ SEXO
    # -----------------------
    if sexo:
        sexo = sexo.lower()
        if sexo == "masculino":
            score += 1
            fatores.append("risco cardiovascular masculino")
        elif sexo == "feminino" and idade and idade >= 55:
            score += 1
            fatores.append("risco aumentado de AVC pós-menopausa")

    # -----------------------
    # 🚨 CLASSIFICAÇÃO FINAL
    # -----------------------
    if score >= 10:
        nivel = "ALTO"
        mensagem = (
            "🚨 RISCO ALTO DETECTADO. "
            "Sintomas compatíveis com AVC ou Infarto. "
            "Procure atendimento médico imediato ou ligue 192 (SAMU)."
        )
    elif score >= 6:
        nivel = "MODERADO"
        mensagem = (
            "⚠️ RISCO MODERADO. "
            "Recomenda-se avaliação médica o quanto antes."
        )
    else:
        nivel = "BAIXO"
        mensagem = (
            "✅ RISCO BAIXO no momento. "
            "Continue monitorando os sintomas."
        )

    return {
        "risk_level": nivel,
        "risk_score": score,
        "fatores_identificados": fatores,
        "mensagem": mensagem
    }
