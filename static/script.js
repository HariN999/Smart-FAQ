document.getElementById("chat-toggle").addEventListener("click", function () {
    document.getElementById("chatbot").style.display = "flex";
});

document.getElementById("close-chat").addEventListener("click", function () {
    document.getElementById("chatbot").style.display = "none";
});

document.getElementById("send-btn").addEventListener("click", function () {
    let inputField = document.getElementById("user-input");
    let userMessage = inputField.value.trim();
    
    if (userMessage === "") return;

    addMessage("You", userMessage);
    inputField.value = "";

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userMessage })
    })
    .then(response => response.json())
    .then(data => addMessage("Bot", data.answer))
    .catch(() => addMessage("Bot", "Sorry, something went wrong."));
});

function addMessage(sender, text) {
    let chatBody = document.getElementById("chat-body");
    let messageDiv = document.createElement("div");
    messageDiv.innerHTML = `<strong>${sender}:</strong> ${text}`;
    chatBody.appendChild(messageDiv);
    chatBody.scrollTop = chatBody.scrollHeight;
}
