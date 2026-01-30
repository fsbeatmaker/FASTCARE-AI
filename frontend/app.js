const button = document.getElementById("btnTexto");
const textarea = document.getElementById("textoInput");
const idadeInput = document.getElementById("idadeInput");
const sexoInput = document.getElementById("sexoInput");

button.addEventListener("click", async () => {
    const texto = textarea.value;
    const idade = idadeInput.value ? parseInt(idadeInput.value) : undefined;
    const sexo = sexoInput.value || undefined;

    if (!texto) {
        alert("Descreva os sintomas.");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/triage/text", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: texto, idade, sexo })
        });

        if (!response.ok) {
            alert("Erro na triagem. Verifique o backend.");
            return;
        }

        const data = await response.json();
        const resultado = data.resultado;

        // Redirecionamento automático
        if (resultado.risk_level.toLowerCase() === "baixo") {
            window.location.href = "/triagem_baixo.html";
        } else if (resultado.risk_level.toLowerCase() === "moderado") {
            window.location.href = "/triagem_moderado.html";
        } else if (resultado.risk_level.toLowerCase() === "alto") {
            window.location.href = "/triagem_alto.html";
        }
    } catch (error) {
        alert("Erro ao chamar a API: " + error);
    }
});
