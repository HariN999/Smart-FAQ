function toggleChat() {
    let chatbox = document.getElementById("chatbot-container");
    chatbox.style.display = chatbox.style.display === "none" ? "flex" : "none";
}

function sendQuery() {
    let userQuery = document.getElementById("chat-input").value;
    let chatBody = document.getElementById("chat-body");

    if (userQuery.trim() === "") return;

    let userMessage = `<p><strong>You:</strong> ${userQuery}</p>`;
    chatBody.innerHTML += userMessage;

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: userQuery }),
    })
    .then(response => response.json())
    .then(data => {
        chatBody.innerHTML += `<p><strong>Bot:</strong> ${data.answer}</p>`;
        document.getElementById("chat-input").value = "";
    });
}
