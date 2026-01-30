const chatBody = document.getElementById("chat-body");
const chatInput = document.getElementById("chat-input");
const chatSend = document.getElementById("chat-send");

// Substitua pelo seu API Key do OpenRouter
const OPENROUTER_API_KEY = "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";

chatSend.addEventListener("click", async () => {
    const userMessage = chatInput.value.trim();
    if (!userMessage) return;

    // Mostra a mensagem do usuário
    const userDiv = document.createElement("div");
    userDiv.textContent = "Você: " + userMessage;
    userDiv.style.fontWeight = "700";
    chatBody.appendChild(userDiv);

    chatInput.value = "";
    chatBody.scrollTop = chatBody.scrollHeight;

    // Chamada API OpenRouter
    try {
        const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${OPENROUTER_API_KEY}`
            },
            body: JSON.stringify({
                model: "gpt-4o-mini",
                messages: [{ role: "user", content: userMessage }]
            })
        });

        const data = await response.json();
        const botMessage = data.choices?.[0]?.message?.content || "Erro ao responder.";

        const botDiv = document.createElement("div");
        botDiv.textContent = "FastCare AI: " + botMessage;
        chatBody.appendChild(botDiv);
        chatBody.scrollTop = chatBody.scrollHeight;

    } catch (err) {
        const botDiv = document.createElement("div");
        botDiv.textContent = "Erro na conexão com o chatbot.";
        chatBody.appendChild(botDiv);
    }
});

